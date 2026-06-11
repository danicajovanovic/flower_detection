from pathlib import Path
from ultralytics import YOLO


BASE_DIR = Path(__file__).resolve().parents[1]

DATA_PATH = BASE_DIR / "data" / "data_colab.yaml"
PROGRESS_IMAGES = BASE_DIR / "inputs" / "progress"
PROGRESS_RESULTS = BASE_DIR / "results" / "training_progress"

EPOCHS_TO_SAVE = {1, 5, 10, 50, 100, 150}


def save_progress_predictions(trainer):
    epoch = trainer.epoch + 1

    if epoch not in EPOCHS_TO_SAVE:
        return

    save_dir = PROGRESS_RESULTS / f"epoch_{epoch}"

    trainer.model.predict(
        source=str(PROGRESS_IMAGES),
        conf=0.25,
        save=True,
        project=str(save_dir),
        name="predictions"
    )

    print(f"Saved progress predictions for epoch {epoch}")


def main():
    model = YOLO("yolov8n.pt")

    model.add_callback("on_train_epoch_end", save_progress_predictions)

    model.train(
        data=str(DATA_PATH),
        epochs=250,
        imgsz=640,
        batch=8,
        patience=20,
        project=str(BASE_DIR / "runs"),
        name="flower_detection_yolov8n",
        plots=True
    )


if __name__ == "__main__":
    main()