from PIL import Image
from src.common.image_resize import ImageResize
from src.common.image_rotate import ImageRotate
from src.common.image_blur import ImageBlur
import base64
import io

class Img:
    ACTIONS = [ImageResize(), ImageRotate(), ImageBlur()]
    def __init__(self, image, event, parameters_group_name):
        self.__img = self.__load_image(image)
        self.__format = self.__img.format
        self.__event = event
        self.__parameters_group_name = parameters_group_name

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

    @property
    def format(self):
        return self.__format
        
    def change(self):
        action = self.__get_action()
        if not action:
            return
        actions = {a.name: a for a in self.ACTIONS}
        if action not in actions.keys():
            raise ValueError(f"Action {action} not supported")
        params = self.__get_parameters(actions[action])
        self.__img = actions[action].execute(self.__img, params)

    def __get_action(self):
        params = self.__event.get(self.__parameters_group_name, {})
        if not isinstance(params, dict):
            return
        return params.get("action", None)

    def __get_parameters(self, action):
        return {p: self.__event.get(self.__parameters_group_name, {}).get(p, None) for p in action.params}

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
