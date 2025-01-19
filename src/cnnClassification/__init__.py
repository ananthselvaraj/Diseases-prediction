import sys
import os
import logging


logging_str = '[%(asctime)s: %(levelname)s: %(module)s: %(message)s ]'

log_path = os.path.join('logs/log_detail.log')
os.makedirs(os.path.dirname(log_path),exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_path),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger('cnnClassificationlogger')