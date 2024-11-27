from ultralytics import YOLO


def main() -> None:
    model = YOLO("yolov8n.pt")
    model.train(data="data\\config.yaml", epochs=1, project="runs")
    # results = model.val()  # evaluate model performance on the validation set
    # results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
    # success = model.export(format="onnx")  # export the model to ONNX format


if __name__ == "__main__":
    main()