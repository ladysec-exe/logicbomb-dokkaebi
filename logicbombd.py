import subprocess
import time
import os
import pygame
from PIL import Image

def is_dev_conn():
    try:
        result = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        devices = result.stdout.splitlines()
        for device in devices:
            if '5555' in device:
                return True
        return False
    except Exception as e:
        print(f"Error checking device: {e}")
        return False

def show_img():
    try:
        image_path = 'dokkaebi_image.png'
        image = Image.open(image_path)
        image.show()
    except Exception as e:
        print(f"Error displaying image: {e}")

def haptic_feedback(duration=0.5, intensity=1.0):
    pygame.init()
    pygame.mixer.init()

    sound = pygame.mixer.Sound(pygame.sndarray.make_sound(pygame.sndarray.array([intensity] * 1000)))
    sound.play(maxtime=int(duration * 1000))

    time.sleep(duration)

    pygame.quit()

def adb_vib():
    try:
        subprocess.run(['adb', 'shell', 'cmd', 'vibrator', 'vibrate', '500'])
    except Exception as e:
        print(f"Error triggering ADB vibration: {e}")

def dokabil():
    if is_dev_conn():
        print("Device connected. 까불지 마...")

        show_img()

        print("Triggering haptic feedback...")
        adb_vib()
        haptic_feedback()

        time.sleep(2)

        print("Hacked!!!")
    else:
        print("No device connected or not listening on port 5555.")

if __name__ == "__main__":
    dokabil()