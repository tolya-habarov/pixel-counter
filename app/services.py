import numpy as np
from PIL import Image
from typing import Tuple


def get_pixel_count(
    file_path: str,
    white_pixel: Tuple[int, int, int]=(255, 255, 255),
    black_pixel: Tuple[int, int, int]=(0, 0, 0),
    ) -> Tuple[int, int]:
    """Return bright and black pixel count

    Args:
        file_path (str): Path to image file
        bright_pixel (int, optional): White pixel. Defaults to (255, 255, 255).
        black_pixel (int, optional): Black pixel. Defaults to (0, 0, 0).

    Returns:
        Tuple[int, int]: Bright, black pixel count
    """

    np_img = _open_image(file_path)
    white_count = _pixel_count_by_color(np_img, white_pixel)
    black_count = _pixel_count_by_color(np_img, black_pixel)

    return white_count, black_count


def pixel_count_by_hex(file_path: str, hex_color: str) -> int:
    """Return pixel count by hex color format

    Args:
        file_path (str): Path to image file
        hex_color (str): Color in hex format

    Returns:
        int: Pixel count
    """

    np_img = _open_image(file_path)
    rgb_color = _hex_to_rgb(hex_color)
    return _pixel_count_by_color(np_img, rgb_color)


def _open_image(file_path: str) -> np.ndarray:
    img = Image.open(file_path)
    if img.mode == 'RGBA':
        img.load()
        background = Image.new("RGB", img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[3])
        img = background

    return np.array(img)


def _pixel_count_by_color(np_img: np.ndarray, rgb_color: Tuple[int, int, int]) -> int:
    return round(np.sum(np_img == rgb_color) / 3) # rgb have 3 channel


def _hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    hex = hex_color.lstrip('#')
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))