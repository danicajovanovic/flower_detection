from pathlib import Path
from ultralytics import YOLO


BASE_DIR = Path(__file__).resolve().parents[1]

WEIGHTS_DIR = (
    BASE_DIR
    / "runs"
    / "flower_detection_yolov8n_from_scratch"
    / "weights"
)

PROGRESS_IMAGES = BASE_DIR / "progress"
OUTPUT_DIR = BASE_DIR / "results" / "training_progress"

EPOCHS_TO_SHOW = [1, 5, 10, 50, 100, 150, 196, 200, 239]


def main():
    if not PROGRESS_IMAGES.exists():
        raise FileNotFoundError(
            f"Folder sa slikama za progres ne postoji: {PROGRESS_IMAGES}"
        )

    for epoch in EPOCHS_TO_SHOW:
        checkpoint = WEIGHTS_DIR / f"epoch{epoch}.pt"

        if not checkpoint.exists():
            print(f"Checkpoint ne postoji za epohu {epoch}: {checkpoint}")
            continue

        model = YOLO(str(checkpoint))

        model.predict(
            source=str(PROGRESS_IMAGES),
            conf=0.4,
            save=True,
            project=str(OUTPUT_DIR),
            name=f"epoch_{epoch}",
            exist_ok=True
        )

        print(f"Sačuvane predikcije za epohu {epoch}")


if __name__ == "__main__":
    main()