from datetime import datetime
import os
import app.helpers.utils as utils


def get_logger():
    # log folder path
    LOG_FOLDER = "./logs/"

    # create log folder
    if os.path.exists(LOG_FOLDER) is False:
        os.mkdir(LOG_FOLDER)

    logger = utils.create_logger(
        (LOG_FOLDER + datetime.now().strftime("%Y-%m-%d--%H-%M-%S") + ".log")
    )
    return logger
