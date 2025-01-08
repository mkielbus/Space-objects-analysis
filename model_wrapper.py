from ultralytics import YOLO
from pathlib import Path


PROJECT_DIR = Path(__file__).parent
MODEL_DIR = PROJECT_DIR/"models"
IMG_DIR = PROJECT_DIR/"static/results"


class ModelWrapper():

    _model: YOLO

    def __init__(self, model_name: str) -> None:
        self._model = YOLO(MODEL_DIR/model_name)

    def predict(self, image_file):
        image_file.save(IMG_DIR/image_file.filename)
        result = self._model.predict(IMG_DIR/image_file.filename)[0]
        result.save(IMG_DIR/f"result_{image_file.filename}")