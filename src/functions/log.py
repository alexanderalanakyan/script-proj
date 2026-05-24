import sys
import logging

sys.path.append("libs")
from rich.logging import RichHandler

logging.basicConfig(
    level="NOTSET",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)

logger = logging.getLogger("rich")


def log(msg="None", level=logging.NOTSET):
    if level == logging.NOTSET:
        logger.info(msg)
    elif level == logging.DEBUG:
        logger.debug(msg)
    elif level == logging.INFO:
        logger.info(msg)
    elif level == logging.ERROR:
        logger.error(msg)
    elif level == logging.CRITICAL:
        msg += "\n a fatal error has happened exiting..."
        logger.critical(msg)
