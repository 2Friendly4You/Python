import time

import cv2
import d3dshot
import keyboard
import mouse

from PIL import ImageGrab


def repress_mouse():
    mouse.release(button='left')
    mouse.press(button='left')


counter = 0

screenshot_x1 = 0
screenshot_y1 = 600
screenshot_x2 = 600
screenshot_y2 = 900

d = d3dshot.create(capture_output="numpy")

print('Starting in 3...')
time.sleep(1)
print('2...')
time.sleep(1)
print('1...')
time.sleep(1)
print('GO!')

# get screenshot of game window program LDPlayer
im = ImageGrab.grab(bbox=(screenshot_x1, screenshot_y1, screenshot_x2, screenshot_y2))
im.save("screenshot.png", 'PNG')

method = cv2.TM_SQDIFF_NORMED

# Read the images from the file
small_image = cv2.imread('screensearch.png')
large_image = cv2.imread('screenshot.png')

result = cv2.matchTemplate(small_image, large_image, method)

# We want the minimum squared difference
mn, _, mnLoc, _ = cv2.minMaxLoc(result)

# Draw the rectangle:
# Extract the coordinates of our best match
MPx, MPy = mnLoc

# Move Mouse to the center of the match
mouse.move((MPx + small_image.shape[1] / 2) + screenshot_x1, (MPy + small_image.shape[0] / 2) + screenshot_y1)

# press and hold left mouse button
mouse.press(button='left')

while True:
    # get image of screen of game window
    im = ImageGrab.grab(bbox=(screenshot_x1, screenshot_y1, screenshot_x2, screenshot_y2))
    try:
        im.save("screenshot.png", 'PNG')
    except:
        print("Error, repressing mouse")
        repress_mouse()

    method = cv2.TM_SQDIFF_NORMED

    # Read the images from the file
    small_image = cv2.imread('screensearch.png')
    large_image = cv2.imread('screenshot.png')

    result = cv2.matchTemplate(small_image, large_image, method)

    # We want the minimum squared difference
    mn, _, mnLoc, _ = cv2.minMaxLoc(result)

    # Draw the rectangle:
    # Extract the coordinates of our best match
    MPx, MPy = mnLoc

    # Move Mouse to the center of the match
    mouse.move((MPx + small_image.shape[1] / 2) + screenshot_x1, (MPy + small_image.shape[0] / 2) + screenshot_y1)

    # if q is pressed, exit
    if keyboard.is_pressed('q'):
        mouse.release(button='left')
        break

    # if r is pressed repress left mouse button
    if keyboard.is_pressed('r'):
        repress_mouse()

    # count to 1000 and then press left mouse button
    counter += 1
    if counter == 500:
        repress_mouse()
        counter = 0
    # print("FPS: ", 1.0 / (time.time() - start_time))
