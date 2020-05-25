from PIL import Image
from .image_action import AbstractImageAction
from .validators import isnumeric

class ImageResize(AbstractImageAction):
    NEEDED_PARAMS = {
        "width": isnumeric,
        "height": isnumeric
    }

    @property
    def name(self):
        return "resize"

    @property
    def params(self):
        return ImageResize.NEEDED_PARAMS.keys()

    def execute(self, image: Image, params):
        super().validate(params, ImageResize.NEEDED_PARAMS.items())
        width = int(params["width"])
        height = int(params["height"])
        img = image.resize((width, height), Image.ANTIALIAS)
        return img
