import PIL
from .image_action import AbstractImageAction
from .validators import isnumeric

class ImageResize(AbstractImageAction):
    NEEDED_PARAMS = (
        ("width", isnumeric),
        ("height", isnumeric)
    )

    def execute(self, image: PIL.Image, params):
        self.__validate(params)
        width = int(params["width"])
        height = int(params["height"])
        img = image.resize((width, height), PIL.Image.ANTIALIAS)
        return img
        
    def __validate(self, params):
        for val in ImageResize.NEEDED_PARAMS:
            if val[0] not in params.keys() or not params[val[0]]:
                raise ValueError(f"{val[0]} parameter missing in input")
            if not val[1](params[val[0]]):
                raise ValueError(f"{val[0]} has wrong type or value")
    