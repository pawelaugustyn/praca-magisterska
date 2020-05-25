from src.common.image_rotate import ImageRotate
from PIL import Image
import unittest

class TestImageRotating(unittest.TestCase):
    def test_missing_input(self):
        img = Image.open("test/testImage.png")
        with self.assertRaises(ValueError):
            ImageRotate().execute(img, {
                "side": ""
            })
        img.close()

    def test_incorrect(self):
        img = Image.open("test/testImage.png")
        with self.assertRaises(ValueError):
            ImageRotate().execute(img, {
                "side": "incorrect-direction"
            })
        img.close()

    def test_correct_rotation(self):
        img = Image.open("test/testImage.png")
        width, height = img.size
        rotated = ImageRotate().execute(img, {
            "side": "left"
        })
        rotated_width, rotated_height = rotated.size
        self.assertEqual(rotated_width, height)
        self.assertEqual(rotated_height, width)
        img.close()
        rotated.close()
