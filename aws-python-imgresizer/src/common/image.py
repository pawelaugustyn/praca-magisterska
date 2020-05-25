from PIL import Image
from src.common.image_resize import ImageResize
import base64
import io

QUERY_STRING_PARAMETERS = "queryStringParameters"

class Img:
    ACTIONS = {
        "resize": {
            "handler": ImageResize,
            "parameters": (
                (QUERY_STRING_PARAMETERS, "width"),
                (QUERY_STRING_PARAMETERS, "height")
            )
        }
    }
    def __init__(self, image, event):
        self.__img = self.__load_image(image)
        self.__format = self.__img.format
        self.__event = event

    def getBytes(self):
        buffered = io.BytesIO()
        try:
            self.__img.save(buffered, format=self.__img.format)
        except ValueError:
            self.__img.save(buffered, format=self.__format)
        buffered.seek(0)
        return buffered

    @property
    def size(self):
        return self.__img.size
        
    def change(self):
        action = self.__get_action()
        if not action:
            return
        if action not in self.ACTIONS.keys():
            raise ValueError(f"Action {action} not supported")
        params = self.__get_parameters(action)
        self.__img = self.ACTIONS[action]["handler"]().execute(self.__img, params)

    def __action_provided(self):
        return self.__event.get(QUERY_STRING_PARAMETERS, {}).get("action", "") > 0

    def __get_action(self):
        return self.__event.get(QUERY_STRING_PARAMETERS, {}).get("action", None)

    def __get_parameters(self, action):
        return {p[1]: self.__event.get(p[0], {}).get(p[1], None) for p in self.ACTIONS.get(action, {}).get("parameters", [])}

    @staticmethod
    def __load_image(img):
        if isinstance(img, Image.Image):
            return img
        img = Image.open(io.BytesIO(img))
        # if img.mode in ('RGBA', 'LA'):
        #     img = img.convert("RGB")
            # background = Image.new(img.mode[:-1], img.size, fill_color)
            # background.paste(img, img.split()[-1])
            # img = background
        return img
