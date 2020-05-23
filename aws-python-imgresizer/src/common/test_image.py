import unittest
import image

class TestImageResizing(unittest.TestCase):
    def test_loaded_image_resize(self):
        dest_width = 320
        dest_height = 240

        img = image.Img("test/testImage.png")
        resized = img.resized(dest_width, dest_height)
        width, height = resized.size
        self.assertEqual(width, dest_width)
        self.assertEqual(height, dest_height)
