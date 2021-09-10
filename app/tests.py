import numpy as np
from PIL import Image

from django.test import TestCase

from app import services


class FindColorTestCase(TestCase):
    def test_find_white_color(self):
        white_color = (255, 255, 255)
        np_img = np.array(Image.new('RGB', (1, 1), white_color))

        pixel_count = services._pixel_count_by_color(np_img, white_color)

        self.assertEqual(pixel_count, 1)

    def test_hex_to_rgb(self):
        hex_color = '#000000'

        rgb_color = services._hex_to_rgb(hex_color)

        self.assertEqual(rgb_color, (0, 0, 0))
