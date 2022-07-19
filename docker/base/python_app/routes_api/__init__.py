import logging

logger = logging.getLogger(__name__)
def includeme(config):
    logger.info("Setting routes for routes api")
    config.include('.views')
    config.scan()