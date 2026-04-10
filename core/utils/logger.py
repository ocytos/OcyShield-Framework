import logging
import os
from datetime import datetime

if not os.path.exists("logs"):
    os.makedirs("logs")

log_file = f"logs/ocyshield_{datetime.now().strftime('%Y%m%d')}.log"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("OcyShield")

def log_status(msg): logger.info(msg)
def log_error(msg): logger.error(msg)
def log_warning(msg): logger.warning(msg)
