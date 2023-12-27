import os
from pathlib import Path
import pyautogui

photo_path = str(Path.home() / 'Pictures/')
screenshot_path = str(Path.home() / 'Pictures/Screenshots/')
screenshot_name = os.system('$(date "+%Y%m%d_%H%M%S")')


def increase_volume():
    os.system(f"pactl set-sink-volume @DEFAULT_SINK@ +20%")

def decrease_volume():
    os.system(f"pactl set-sink-volume @DEFAULT_SINK@ -20%")

def increase_brightness():
    os.system(f"xrandr --output $(xrandr | grep primary | awk '{{print $1}}') --brightness 1")

def decrease_brightness():
    os.system(f"xrandr --output $(xrandr | grep primary | awk '{{print $1}}') --brightness 0.5")

def take_photo():
    os.system(f'fswebcam -r 1280x720 --no-banner {photo_path}/$(date "+%Y%m%d_%H%M%S").jpg')


def take_screenshot(file_path=f"{screenshot_path}/{screenshot_name}.png"):
    # Get the screen size
    screen_width, screen_height = pyautogui.size()

    # Take a screenshot
    screenshot = pyautogui.screenshot()

    # Save the screenshot to a file
    screenshot.save(file_path)

    print(f"Screenshot saved to {file_path}")

