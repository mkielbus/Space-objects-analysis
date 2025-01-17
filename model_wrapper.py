from ultralytics import YOLO
from config import MODELS_DIR, IMG_DIR


class ModelWrapper():
    """
    Class wrapping YOLO model, providing usefull methods for usage in the webservice.
    """
    _model: YOLO

    def __init__(self, model_name: str) -> None:
        self._model = YOLO(MODELS_DIR/model_name)

    def predict(self, image_file):
        """
        Performs prediction on the image file. Both input and output images are saved in the IMG_DIR directory.
        Input images is saved under original name, the output image is saved under the name result_{original_name}.
        """
        image_file.save(IMG_DIR/image_file.filename)
        result = self._model.predict(IMG_DIR/image_file.filename)[0]
        result.save(IMG_DIR/f"result_{image_file.filename}")