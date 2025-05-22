import logging
from typing import Union

def setup_logger(level: Union[str, int] = logging.INFO):
    """
    Konsolga log yozishni sozlaydi.
    
    :param level: log darajasi — 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL' yoki int
    """
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    logging.getLogger("apscheduler").setLevel(logging.WARNING)  # Jadval loglarini kamaytirish
    logging.getLogger("aiogram.event").setLevel(logging.WARNING)  # Aiogram hodisa loglarini kamaytirish
