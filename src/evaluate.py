from ultralytics import YOLO

MODEL_PATH = "models/best.pt"
DATA_PATH = "data/data_local.yaml"


def main():
    model = YOLO(MODEL_PATH)

    model.val(
        data=DATA_PATH,
        split="test",
        project="results",
        name="evaluation"
    )

    print("Evaluacija je završena.")


if __name__ == "__main__":
    main()