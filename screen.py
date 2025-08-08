
from mss import mss
from image import get_red_pixels_sum
from time import perf_counter, sleep
import keyboard


def grab_screen(width, height, offset_x, offset_y, shared_red_sum, trigger_key: str, target_hz: int = 300):
    screen_mss = mss()
    bounding_box = {
        'top': height // 2 - offset_y,
        'left': width // 2 - offset_x,
        'width': offset_x * 2,
        'height': offset_y * 2,
    }

    min_frame_time = 1.0 / max(1, target_hz)
    next_time = perf_counter()

    while True:
        # Захват только при зажатом триггере, чтобы снизить нагрузку вне боя
        if not keyboard.is_pressed(trigger_key):
            shared_red_sum.value = 0
            sleep(0.001)
            continue

        start = perf_counter()

        sct_img = screen_mss.grab(bounding_box)
        red_sum = int(get_red_pixels_sum(sct_img))
        shared_red_sum.value = red_sum

        # Ограничение частоты кадров
        next_time += min_frame_time
        remaining = next_time - start
        if remaining > 0:
            sleep(remaining)
        else:
            # если не успеваем, сдвигаем окно, чтобы не накапливалось отставание
            next_time = perf_counter()
