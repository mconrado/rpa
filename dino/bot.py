import pyautogui
from PIL import ImageGrab
import time


def isColision(data):
    for i in range(490, 535):
        for j in range(345, 375):
            if data[i, j] < 100:
                print("pulando")
                pyautogui.keyDown("up")
                return
    return


if __name__ == "__main__":
    while True:
        image = ImageGrab.grab().convert("L")
        data = image.load()
        isColision(data)
        time.sleep(0.03)
        """
        for i in range(490, 535):
            for j in range(340, 375):
                data[i, j] = 0

        image.show()
        break
    """
