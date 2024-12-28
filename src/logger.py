# logger.py
import logging

# Configure the logger
LOG_FORMAT = "%(asctime)s - %(filename)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# Create a logger object
logger = logging.getLogger("app_logger")

# Optional: Configure logging to a file
# file_handler = logging.FileHandler("app.log")
# file_handler.setLevel(logging.INFO)
# file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
# logger.addHandler(file_handler)

# Avoid duplicate logs in the console
# logger.propagate = False
