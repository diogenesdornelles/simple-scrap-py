import logging
import os

from constants import DIR

# from time import time

TARGET_DIR = os.path.join(DIR, "logs")


class ColorCodes:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'


class ColoredConsoleHandler(logging.StreamHandler):
    def emit(self, record):
        try:
            message = self.format(record)
            level = record.levelname

            if level == 'INFO':
                message = f"{ColorCodes.GREEN}{message}{ColorCodes.RESET}"
            elif level == 'DEBUG':
                message = f"{ColorCodes.BLUE}{message}{ColorCodes.RESET}"
            elif level == 'WARNING':
                message = f"{ColorCodes.YELLOW}{message}{ColorCodes.RESET}"
            elif level == 'ERROR' or level == 'CRITICAL':
                message = f"{ColorCodes.RED}{message}{ColorCodes.RESET}"
            print(message)
        except Exception:
            self.handleError(record)


"""set_logging _summary_"""
if not os.path.exists(TARGET_DIR):
    os.mkdir(TARGET_DIR)

# create logger

logger = logging.getLogger('LOG MESSAGE')
logger.setLevel(logging.DEBUG)


console_handler = ColoredConsoleHandler()


# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler.setFormatter(formatter)

logger.addHandler(console_handler)
