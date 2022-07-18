import logging

logger = logging.getLogger(__name__)
def includeme(config):
    logger.info("Setting routes")
    config.include('.views')
    config.scan()
    