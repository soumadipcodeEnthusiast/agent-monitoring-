import logging
from app.core.config import settings

logging.basicConfig(level=settings.log_level)
logger = logging.getLogger("afde")
