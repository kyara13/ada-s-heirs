"""Etapa 4: género percibido y edad estimada a partir de la cara de cada persona seguida.

- Usamos el código de InsightFace (MIT); sus modelos preentrenados son de uso no comercial,
  así que no los incluimos en el repositorio: se descargan la primera vez.
- Procesamos las caras en memoria y las descartamos: no guardamos recortes ni embeddings.
- El resultado es el género percibido por un modelo, no la identidad de género.

Salida: caras.json
"""

from collections import defaultdict

from .utils import iter_frames, load_json, resolve_device, save_json


class InsightFaceAnalyzer:
    def __init__(self, min_face_score=0.5, device="auto"):
        from insightface.app import FaceAnalysis
        providers = (["CUDAExecutionProvider", "CPUExecutionProvider"]
                     if resolve_device(device) == "cuda" else ["CPUExecutionProvider"])
        self.app = FaceAnalysis(name="buffalo_l", providers=providers,
                                allowed_modules=["detection", "genderage"])
        self.app.prepare(ctx_id=0 if "CUDAExecutionProvider" in providers else -1,
                         det_size=(640, 640))
        self.min_face_score = min_face_score

    def analyze(self, crop_bgr):
        """Devuelve la cara más grande del recorte, o None."""
        faces = [f for f in self.app.get(crop_bgr) if f.det_score >= self.min_face_score]
        if not faces:
            return None
        face = max(faces, key=lambda f: (f.bbox[2] - f.bbox[0]) * (f.bbox[3] - f.bbox[1]))
        gender = {1: "hombre", 0: "mujer"}.get(int(face.gender)) if face.gender is not None else None
        return {"gender": gender, "age": float(face.age) if face.age is not None else None,
                "face_score": float(face.det_score),
                "face_box": [float(v) for v in face.bbox]}


def get_analyzer(cfg):
    fcfg = cfg["faces"]
    if fcfg["model"] == "insightface":
        return InsightFaceAnalyzer(fcfg["min_face_score"], fcfg["device"])
    if fcfg["model"] == "none":
        return None
    raise ValueError(f"Analizador facial desconocido: {fcfg['model']}")


def run(video_path, cfg, outdir):
    tracks = load_json(outdir / "tracks.json")
    analyzer = get_analyzer(cfg)
    every_n = cfg["faces"]["every_n_frames"]

    by_frame = defaultdict(list)
    for o in tracks["observations"]:
        by_frame[o["frame"]].append(o)

    seen_per_track = defaultdict(int)
    results = []
    if analyzer is not None:
        for idx, _, frame, scale in iter_frames(video_path, cfg["video"]["fps_sample"],
                                                cfg["video"]["max_side"]):
            for o in by_frame.get(idx, []):
                seen_per_track[o["track_id"]] += 1
                if (seen_per_track[o["track_id"]] - 1) % every_n:
                    continue
                x1, y1, x2, y2 = [int(v * scale) for v in o["box"]]
                crop = frame[max(0, y1):max(0, y2), max(0, x1):max(0, x2)]
                if crop.size == 0:
                    continue
                face = analyzer.analyze(crop)
                if face is None:
                    continue
                fx1, fy1, fx2, fy2 = face["face_box"]
                face["face_box"] = [(fx1 + x1) / scale, (fy1 + y1) / scale,
                                    (fx2 + x1) / scale, (fy2 + y1) / scale]
                results.append({"frame": idx, "track_id": o["track_id"], **face})
                # Aquí descartamos el recorte: no guardamos ninguna imagen de la cara.

    save_json({"observations": results}, outdir / "caras.json")
    print(f"[faces] {len(results)} caras analizadas")
    return results
