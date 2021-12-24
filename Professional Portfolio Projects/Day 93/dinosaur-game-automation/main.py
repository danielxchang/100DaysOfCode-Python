import pyautogui
import mss
import mss.tools

# https://elgoog.im/t-rex/

dino_width = 5
dino_height = 2


class DinosaurBot:
    def __init__(self):
        self.game_region_location = pyautogui.locateOnScreen('game-region.png')
        self.game_region_point = pyautogui.center(self.game_region_location)
        self.game_region = (
            self.game_region_location.left,
            self.game_region_location.top,
            self.game_region_location.width,
            self.game_region_location.height
        )
        self.dino_location = pyautogui.locateOnScreen('dino.png', region=self.game_region)
        self.dino_region = {
            'left': self.dino_location.left + 147,
            'top': self.dino_location.top + 30,
            'width': dino_width,
            'height': dino_height
        }
        self.start_game()

    def start_game(self):
        pyautogui.click(x=self.game_region_point.x, y=self.game_region_point.y)
        pyautogui.press('space')

        while True:
            self.check_for_obstacle()

    def check_for_obstacle(self):
        with mss.mss() as sct:
            sct_img = sct.grab(self.dino_region)
            for x in range(sct_img.width):
                for y in range(sct_img.height):
                    if sct_img.pixel(x, y)[0] != 247:
                        pyautogui.press('space')
                        break


bot = DinosaurBot()
