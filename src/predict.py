from ultralytics import YOLO

MODEL_PATH = "models/best.pt"
SOURCE_PATH = "inputs/test.jpg"


def main():
    model = YOLO(MODEL_PATH)

    model.predict(
        source=SOURCE_PATH,
        conf=0.4,
        save=True,
        project="results",
        name="prediction"
    )

    print("Predikcija je završena.")


if __name__ == "__main__":
    main()