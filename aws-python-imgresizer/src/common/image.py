from PIL import Image 
import base64
import io

class Img:
    def __init__(self, image):
        self.__img = self.__load_image(image)

    def getBytes(self):
        buffered = io.BytesIO()
        return self.__img.save(buffered)

    @property
    def size(self):
        return self.__img.size

    def resized(self, width, height):
        if width is None or height is None:
            return Img(self.__img)
        img = self.__img.resize((width, height), Image.ANTIALIAS)
        return Img(img)

    @staticmethod
    def __load_image(img):
        if isinstance(img, Image.Image):
            return img
        img = Image.open(img)
        return img
