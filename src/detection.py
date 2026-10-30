"""Etapa 2: detección de personas en cada fotograma analizado.

Guardamos las cajas en píxeles de la resolución original del vídeo.

Salida: detecciones.json
"""

from .utils import iter_frames, load_json, resolve_device, save_json, shot_for_time, video_info


class TorchvisionFasterRCNN:
    """Faster R-CNN de torchvision (BSD), preentrenado en COCO. La clase 1 es persona."""

    PERSON_LABEL = 1

    def __init__(self, min_score=0.6, device="auto", light=False):
        import torch
        from torchvision.models import detection as tvd
        self.torch = torch
        self.device = resolve_device(device)
        if light:   # MobileNetV3: más rápido en CPU, algo menos preciso
            weights = tvd.FasterRCNN_MobileNet_V3_Large_FPN_Weights.DEFAULT
            model = tvd.fasterrcnn_mobilenet_v3_large_fpn(weights=weights)
        else:       # ResNet50 v2: más preciso, para GPU
            weights = tvd.FasterRCNN_ResNet50_FPN_V2_Weights.DEFAULT
            model = tvd.fasterrcnn_resnet50_fpn_v2(weights=weights)
        self.model = model.to(self.device).eval()
        self.min_score = min_score

    def detect(self, frame_bgr):
        import cv2
        rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)   # OpenCV lee en BGR
        tensor = self.torch.from_numpy(rgb).permute(2, 0, 1).float().div(255).to(self.device)
        with self.torch.no_grad():
            out = self.model([tensor])[0]
        boxes = []
        for box, label, score in zip(out["boxes"], out["labels"], out["scores"]):
            if int(label) == self.PERSON_LABEL and float(score) >= self.min_score:
                x1, y1, x2, y2 = [float(v) for v in box]
                boxes.append([x1, y1, x2, y2, float(score)])
        return boxes


def get_detector(cfg):
    det_cfg = cfg["detection"]
    if det_cfg["model"] == "torchvision_fasterrcnn":
        return TorchvisionFasterRCNN(min_score=det_cfg["min_score"], device=det_cfg["device"])
    if det_cfg["model"] == "torchvision_fasterrcnn_mobilenet":
        return TorchvisionFasterRCNN(min_score=det_cfg["min_score"], device=det_cfg["device"],
                                     light=True)
    raise ValueError(f"Detector desconocido: {det_cfg['model']}")


def run(video_path, cfg, outdir):
    info = video_info(video_path)
    shots = load_json(outdir / "planos.json")["shots"]
    detector = get_detector(cfg)
    min_area = cfg["detection"]["min_box_ratio"] * info["width"] * info["height"]

    frames = []
    for idx, t, frame, scale in iter_frames(video_path, cfg["video"]["fps_sample"],
                                            cfg["video"]["max_side"]):
        boxes = []
        for x1, y1, x2, y2, s in detector.detect(frame):
            x1, y1, x2, y2 = x1 / scale, y1 / scale, x2 / scale, y2 / scale
            if (x2 - x1) * (y2 - y1) >= min_area:
                boxes.append([x1, y1, x2, y2, s])
        frames.append({"frame": idx, "t": t, "shot_id": shot_for_time(shots, t), "boxes": boxes})

    result = {"video": str(video_path), "width": info["width"], "height": info["height"],
              "fps_sample": cfg["video"]["fps_sample"], "duration_s": info["duration_s"],
              "frames": frames}
    save_json(result, outdir / "detecciones.json")
    n = sum(len(f["boxes"]) for f in frames)
    print(f"[detection] {len(frames)} frames analizados, {n} detecciones de persona")
    return result
