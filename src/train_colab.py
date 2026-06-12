from pathlib import Path
from ultralytics import YOLO


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "data_colab.yaml"


def main():
    model = YOLO("yolov8n.yaml")

    model.train(
        data=str(DATA_PATH),
        epochs=250,
        imgsz=640,
        batch=8,
        patience=20,
        project=str(BASE_DIR / "runs"),
        name="flower_detection_yolov8n_from_scratch",
        plots=True,
        save=True,
        save_period=1
    )


if __name__ == "__main__":
    main()