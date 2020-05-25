from PIL import Image, ImageFilter
from .image_action import AbstractImageAction

class ImageBlur(AbstractImageAction):
    @property
    def name(self):
        return "blur"

    @property
    def params(self):
        return []

    def execute(self, image: Image, params):
        img = image.filter(filter=ImageFilter.BLUR)
        return img
    