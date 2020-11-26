import logging
import hashlib


def hash(message):
    if message is not None and message != "":
        return hashlib.sha256(message.encode("utf-8")).hexdigest()


def tweets_to_list(tweets):
    return [x.json() for x in tweets]


def create_logger(path):

    logger = logging.getLogger()

    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler(path)

    # Create formatters and add it to handlers
    f_format = logging.Formatter(
        "%(asctime)s %(levelname)s %(filename)s %(lineno)d %(message)s"
    )

    f_handler.setFormatter(f_format)

    # Set logging level
    logger.setLevel(logging.DEBUG)
    c_handler.setLevel(logging.INFO)
    f_handler.setLevel(logging.DEBUG)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger
