import logging
from pathlib import Path

# ----------------------------------------------------
# Create logs folder
# ----------------------------------------------------

Path("logs").mkdir(exist_ok=True)

# ----------------------------------------------------
# Create CiteWise logger
# ----------------------------------------------------

logger = logging.getLogger("CiteWise")

logger.setLevel(logging.INFO)

# Prevent duplicate logs
logger.propagate = False

# ----------------------------------------------------
# Formatter
# ----------------------------------------------------

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

# ----------------------------------------------------
# File Handler
# ----------------------------------------------------

file_handler = logging.FileHandler(
    "logs/pipeline.log",
    encoding="utf-8"
)

file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

# ----------------------------------------------------
# Console Handler
# ----------------------------------------------------

console_handler = logging.StreamHandler()

console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# ----------------------------------------------------
# Avoid duplicate handlers
# ----------------------------------------------------

if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

# ----------------------------------------------------
# Silence noisy third-party libraries
# ----------------------------------------------------

logging.getLogger("sentence_transformers").setLevel(logging.WARNING)
logging.getLogger("transformers").setLevel(logging.WARNING)
logging.getLogger("huggingface_hub").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("chromadb").setLevel(logging.WARNING)