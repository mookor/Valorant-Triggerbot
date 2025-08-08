import numpy as np


def get_red_pixels_sum(sct_img, min_red: int = 230, max_green: int = 230, max_blue: int = 230) -> np.uint8:
    """Fast red pixel intensity estimation without in-place array mutations.

    Uses MSS ScreenShot.rgb (RGB order) with zero-copy view to minimize memory traffic,
    then computes an average red intensity over the whole image, keeping only pixels
    that satisfy the thresholds.
    """
    try:
        height = sct_img.height
        width = sct_img.width

        # Zero-copy view of RGB bytes
        arr = np.frombuffer(sct_img.rgb, dtype=np.uint8).reshape((height, width, 3))

        red_channel = arr[:, :, 0]
        green_channel = arr[:, :, 1]
        blue_channel = arr[:, :, 2]

        mask = (red_channel >= min_red) & (green_channel <= max_green) & (blue_channel <= max_blue)

        red_sum = red_channel[mask].sum(dtype=np.uint32)
        avg_red = red_sum / (height * width)

        return np.uint8(avg_red)
    except Exception:
        return np.uint8(0)