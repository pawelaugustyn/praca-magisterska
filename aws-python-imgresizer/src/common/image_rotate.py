from PIL import Image
from .image_action import AbstractImageAction

class ImageRotate(AbstractImageAction):
    DIRECTIONS = {
        "left": 90,
        "right": -90,
        "top-down": 180
    }
    
    NEEDED_PARAMS = {
        "side": lambda s: s in ImageRotate.DIRECTIONS.keys()
    }

    @property
    def name(self):
        return "rotate"

    @property
    def params(self):
        return ImageRotate.NEEDED_PARAMS.keys()

    def execute(self, image: Image, params):
        super().validate(params, ImageRotate.NEEDED_PARAMS.items())
        img = image.rotate(ImageRotate.DIRECTIONS[params["side"]], expand=1)
        return img
    