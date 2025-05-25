import logging
from server.config import Config

def setup_logging():
    config = Config()
    logfile = config.get("LOG_FILE")
    logging.basicConfig(
        filename=logfile,
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
