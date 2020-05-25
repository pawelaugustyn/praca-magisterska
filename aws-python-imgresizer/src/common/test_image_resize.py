from src.common.image_resize import ImageResize
from PIL import Image
import unittest

class TestImageResizing(unittest.TestCase):
    def test_loaded_image_resize(self):
        dest_width = 320
        dest_height = 240

        img = Image.open("test/testImage.png")
        resized = ImageResize().execute(img, {
            "width": dest_width,
            "height": dest_height
        })
        width, height = resized.size
        self.assertEqual(width, dest_width)
        self.assertEqual(height, dest_height)

    def test_non_numeric_input(self):
        dest_width = "320x"
        dest_height = 240

        img = Image.open("test/testImage.png")
        with self.assertRaises(ValueError):
            ImageResize().execute(img, {
                "width": dest_width,
                "height": dest_height
            })
        img.close()

    def test_negative_number(self):
        dest_width = -1
        dest_height = 240

        img = Image.open("test/testImage.png")
        with self.assertRaises(ValueError):
            ImageResize().execute(img, {
                "width": dest_width,
                "height": dest_height
            })
        img.close()

    def test_missing_input(self):
        dest_width = 3

        img = Image.open("test/testImage.png")
        with self.assertRaises(ValueError):
            ImageResize().execute(img, {
                "width": dest_width
            })
        img.close()

