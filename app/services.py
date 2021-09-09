import numpy as np
from PIL import Image
from typing import Tuple


def get_pixel_count(
    file_path: str,
    white_threshold: int=255,
    black_threshold: int=0
    ) -> Tuple[int, int]:
    """Return bright and black pixel count

    Args:
        file_path (str): Path to image file
        bright_threshold (int, optional): Bright pixel threshold. Defaults to 255.
        black_threshold (int, optional): Black pixel threshold. Defaults to 0.

    Returns:
        Tuple[int, int]: Bright, black pixel count
    """

    img = _open_image(file_path)

    np_img = np.array(img)
    white_count = np.sum(np_img >= white_threshold)
    black_count = np.sum(np_img <= black_threshold)

    return white_count, black_count


def pixel_count_by_hex(file_path: str, hex_color: str) -> int:
    """Return pixel count by hex color format

    Args:
        file_path (str): Path to image file
        hex_color (str): Color in hex format

    Returns:
        int: Pixel count
    """

    h = hex_color.lstrip('#')
    rgb_color = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    
    img = _open_image(file_path)
    return np.sum(np.array(img) == rgb_color)


def _open_image(file_path: str):
    img = Image.open(file_path)
    if img.mode == 'RGBA':
        img.load()
        background = Image.new("RGB", img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[3])
        return background

    return img