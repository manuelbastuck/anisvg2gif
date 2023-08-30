import numpy as np
import cv2
from mss import mss
from PIL import Image
import imageio
import webview
import time

from win32gui import FindWindow, GetWindowRect


dims = (100, 100)


def record():
    window_handle = FindWindow(None, "test")
    window_rect   = GetWindowRect(window_handle)
    monitor = {'top': window_rect[1], 'left': window_rect[0], 'width': dims[0]*2, 'height': dims[1]*2}

    sct = mss()
    images = []

    start = time.time()
    last_time = 0
    while True:
        while True:
            if (time.time() - last_time) > 0.04:
                break

        img = Image.frombytes('RGB', (monitor['width'], monitor['height']), sct.grab(monitor).rgb)
        img.resize(dims, Image.BICUBIC)
        images.append(img)

        last_time = time.time()
        if (time.time() - start) > 2:
            break

    print('finished recording')
    imageio.mimwrite('test.gif', images, duration=2000/len(images), loop=0)
    print('finished saving')

window = webview.create_window('test', 'test.svg', frameless=True, width=100, height=200)
window.events.loaded += record
webview.start()