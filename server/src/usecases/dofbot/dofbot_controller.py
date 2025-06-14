import pyautogui as pag

from src.core.models.dofbot import DofbotControl
from src.core.models.config import Config


class DofBotController:
    def __init__(self):
        self.servo1 = 90
        self.servo2 = 90
        self.servo3 = 90
        self.servo4 = 90
        self.servo5 = 90
        self.servo6 = 180

    def set_newtral_position(self):
        """
        Sets the DOFBOT to a neutral position.
        """
        pag.scroll(90-self.servo1, interval=0.02)
        pag.scroll(90-self.servo2, interval=0.02)
        pag.scroll(90-self.servo3, interval=0.02)
        pag.scroll(90-self.servo4, interval=0.02)
        pag.scroll(90-self.servo5, interval=0.02)
        pag.scroll(180-self.servo6, interval=0.02)

    def control_dofbot(self, dofbot: DofbotControl, config: Config) -> None:
        """
        Controls the DOFBOT by sending commands to the robot.
        """
        if dofbot.servo1 < config.min_servo1 or dofbot.servo1 > config.max_servo1:
            print(f"servo1 must be between {config.min_servo1} and {config.max_servo1}")
        else:
            pag.moveTo(config.dofbot_app_servo1_scroll_coodinate[0], config.dofbot_app_servo1_scroll_coodinate[1])
            pag.scroll(dofbot.servo1 - self.servo1, interval=0.02)
            self.servo1 = dofbot.servo1
        if dofbot.servo2 < config.min_servo2 or dofbot.servo2 > config.max_servo2:
            print(f"servo2 must be between {config.min_servo2} and {config.max_servo2}")
        else:
            pag.moveTo(config.dofbot_app_servo2_scroll_coodinate[0], config.dofbot_app_servo2_scroll_coodinate[1])
            pag.scroll(dofbot.servo2 - self.servo2, interval=0.02)
            self.servo2 = dofbot.servo2
        if dofbot.servo3 < config.min_servo3 or dofbot.servo3 > config.max_servo3:
            print(f"servo3 must be between {config.min_servo3} and {config.max_servo3}")
        else:
            pag.moveTo(config.dofbot_app_servo3_scroll_coodinate[0], config.dofbot_app_servo3_scroll_coodinate[1])
            pag.scroll(dofbot.servo3 - self.servo3, interval=0.02)
            self.servo3 = dofbot.servo3
        if dofbot.servo4 < config.min_servo4 or dofbot.servo4 > config.max_servo4:
            print(f"servo4 must be between {config.min_servo4} and {config.max_servo4}")
        else:
            pag.moveTo(config.dofbot_app_servo4_scroll_coodinate[0], config.dofbot_app_servo4_scroll_coodinate[1])
            pag.scroll(dofbot.servo4 - self.servo4, interval=0.02)
            self.servo4 = dofbot.servo4
        if dofbot.servo5 < config.min_servo5 or dofbot.servo5 > config.max_servo5:
            print(f"servo5 must be between {config.min_servo5} and {config.max_servo5}")
        else:
            pag.moveTo(config.dofbot_app_servo5_scroll_coodinate[0], config.dofbot_app_servo5_scroll_coodinate[1])
            pag.scroll(dofbot.servo5 - self.servo5, interval=0.02)
            self.servo5 = dofbot.servo5
        if dofbot.servo6 < config.min_servo6 or dofbot.servo6 > config.max_servo6:
            print(f"servo6 must be between {config.min_servo6} and {config.max_servo6}")
        else:
            pag.moveTo(config.dofbot_app_servo6_scroll_coodinate[0], config.dofbot_app_servo6_scroll_coodinate[1])
            pag.scroll(dofbot.servo6 - self.servo6, interval=0.02)
            self.servo6 = dofbot.servo6
