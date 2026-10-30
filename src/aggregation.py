"""Etapa 5: una etiqueta de género percibido por persona.

En fotogramas sueltos el clasificador se equivoca, así que votamos sobre toda la trayectoria.
Si una etiqueta supera vote_threshold y hay al menos min_votes caras, la asignamos; si no,
la persona queda como "no_determinado". Preferimos reconocer la duda a inventar una etiqueta.

Salida: personas.json
"""

from collections import Counter, defaultdict
from statistics import median

from .utils import load_json, save_json

LABELS = ("mujer", "hombre")
UNKNOWN = "no_determinado"


def aggregate_track(face_obs, vote_threshold=0.8, min_votes=3):
    """face_obs: observaciones de cara de una sola trayectoria."""
    votes = Counter(o["gender"] for o in face_obs if o.get("gender") in LABELS)
    n = sum(votes.values())
    ages = [o["age"] for o in face_obs if o.get("age") is not None]
    age_median = float(median(ages)) if ages else None

    if n < min_votes:
        return {"label": UNKNOWN, "confidence": 0.0, "votes": dict(votes),
                "n_faces": n, "age_median": age_median}

    top_label, top_count = votes.most_common(1)[0]
    confidence = top_count / n
    label = top_label if confidence >= vote_threshold else UNKNOWN
    return {"label": label, "confidence": round(confidence, 3), "votes": dict(votes),
            "n_faces": n, "age_median": age_median}


def aggregate(track_ids, face_observations, vote_threshold=0.8, min_votes=3):
    by_track = defaultdict(list)
    for o in face_observations:
        by_track[o["track_id"]].append(o)
    return [{"track_id": tid, **aggregate_track(by_track.get(tid, []), vote_threshold, min_votes)}
            for tid in sorted(track_ids)]


def run(video_path, cfg, outdir):
    tracks = load_json(outdir / "tracks.json")
    faces = load_json(outdir / "caras.json")["observations"]
    track_ids = {o["track_id"] for o in tracks["observations"]}
    acfg = cfg["aggregation"]
    personas = aggregate(track_ids, faces, acfg["vote_threshold"], acfg["min_votes"])
    save_json({"personas": personas}, outdir / "personas.json")
    counts = Counter(p["label"] for p in personas)
    print(f"[aggregation] {dict(counts)}")
    return personas
