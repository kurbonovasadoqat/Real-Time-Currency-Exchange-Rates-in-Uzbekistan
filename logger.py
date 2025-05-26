# currency_bot/logger.py

import logging
import sys

def setup_logger(level: str = "INFO") -> None:
    """
    Logger konfiguratsiyasi — barcha modullarda yagona log formatini ta’minlaydi.
    
    :param level: 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
    """
    logging.basicConfig(
        level=level.upper(),
        format="🟢 [%(name)s] %(levelname)s: %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout)  # loglarni terminalga chiqarish
        ]
    )

    # Boshqa kutubxonalar logini kamaytirish
    logging.getLogger("aiogram").setLevel(level.upper())
    logging.getLogger("apscheduler").setLevel("WARNING")
    logging.getLogger("aiohttp.access").setLevel("WARNING")
