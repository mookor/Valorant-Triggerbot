
from multiprocessing import Process, Value
import ctypes
from screen import grab_screen
from time import sleep
import keyboard
from config import Config
from app import start_app
from os import _exit





def hold(red_sum, trigger_key, shot_key, sleep_before, sleep_after, threshold=5):
    if red_sum > threshold:
        if keyboard.is_pressed(trigger_key):
            sleep(sleep_before)
            keyboard.press_and_release(shot_key)
            sleep(sleep_after)


if __name__ == '__main__':
    config = Config('config.yaml')
    user32 = ctypes.windll.user32
    width = user32.GetSystemMetrics(0)
    height = user32.GetSystemMetrics(1)

    offset_x = config['offset_x']
    offset_y = config['offset_y']
    sleep_before = config['sleep_before']
    sleep_after = config['sleep_after']
    threshold = config['threshold']
    icon_path = config['icon_path']
    trigger_key = config['trigger_key']
    shot_key = config['shot_key']
    target_hz = config['target_hz']
    img_w = 2 * offset_x
    img_h = 2 * offset_y

    red_sum = Value(ctypes.c_uint8, 0 )

    p = Process(target=grab_screen, args=(width, height, offset_x, offset_y, red_sum, trigger_key, target_hz))
    p.start()

    p2 = Process(target=start_app, args=(icon_path, ))
    p2.start()

    while True:
        hold(red_sum.value, trigger_key, shot_key, sleep_before, sleep_after, threshold)

        if p2.is_alive() == False:
            p.terminate()
            p.join()
            _exit(0)
        sleep(0.0005)
        
        