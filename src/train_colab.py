from ultralytics import YOLO


def main():
    model = YOLO("yolov8n.yaml")

    model.train(
        data="data/data_colab.yaml",
        epochs=250,
        imgsz=640,
        batch=8,
        patience=20,
        project="runs",
        name="flower_detection_yolov8n",
        plots=True
    )


if __name__ == "__main__":
    main()