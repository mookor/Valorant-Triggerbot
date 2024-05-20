
from mss import mss
from image import get_red_pixels_sum
from time import sleep

def grab_screen(width, height, offset_x, offset_y, shared_red_sum):
    screen_mss = mss()
    bounding_box  = {}
    while True:
        bounding_box['top'] = height // 2 - offset_y
        bounding_box['left'] = width // 2 - offset_x
        bounding_box['width'] = offset_x*2
        bounding_box['height'] = offset_y*2
        sct_img = screen_mss.grab(bounding_box)

        red_sum = get_red_pixels_sum(sct_img)

        shared_red_sum.value = red_sum

        sleep(0.0001)
