import logging
from datetime import datetime
from config import settings

def get_group_logger(analysis:str, name: str, timestamp:datetime):

    logger = logging.getLogger(__name__)

    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler(f'logs/{analysis}-{name}-{timestamp.date()}-{timestamp.time().hour}h{timestamp.time().minute}.txt')
    c_handler.setLevel(logging.INFO)
    f_handler.setLevel(logging.INFO)

    c_format = logging.Formatter('%(asctime)s | %(message)s')
    f_format = logging.Formatter('%(asctime)s | %(message)s')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)
    return logger


logger = get_group_logger(settings.NOMBRE_AVANCE, settings.NOMBRE_ESTUDIANTE, datetime.now())