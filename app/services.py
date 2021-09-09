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


def _open_image(file_path: str):
    img = Image.open(file_path)
    if img.mode == 'RGBA':
        img.load()
        background = Image.new("RGB", img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[3])
        return background

    return img