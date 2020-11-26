from datetime import datetime
from helpers.utils import create_logger
import os


def get_logger():
    # log folder path
    LOG_FOLDER = "./logs/"

    # create log folder
    if os.path.exists(LOG_FOLDER) is False:
        os.mkdir(LOG_FOLDER)

    logger = create_logger(
        (LOG_FOLDER + datetime.now().strftime("%Y-%m-%d--%H-%M-%S") + ".log")
    )
    return logger
