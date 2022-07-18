import logging

logger = logging.getLogger(__name__)

def includeme(config):
    logger.info("Including views")
    config.include('.login')
