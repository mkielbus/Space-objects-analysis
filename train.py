from ultralytics import YOLO
from config import MODELS_DIR, DATA_DIR


def main() -> None:
    model = YOLO(MODELS_DIR/"trained_model.pt")
    # model.train(data="data/config.yaml", epochs=1, project="runs")
    model.val(data="data/config.yaml", project="runs")


if __name__ == "__main__":
    main()