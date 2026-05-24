import os
import logging
from datetime import datetime

LOG_DIR = os.path.join(os.getcwd(), 'logs')
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"
log_file = os.path.join(LOG_DIR, LOG_FILE)

logging.basicConfig(
    filename=log_file,
    encoding='utf-8',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.debug("Detailed diagnostic information.")
logging.info("Confirmation that things are working.")
logging.warning("An unexpected issue occurred.")