import logging
from pyramid.response import Response

logger = logging.getLogger(__name__)

def includeme(config):
    logger.info("Including route /geoip")
    config.add_route('geoip_get', "/geoip")
    config.scan('.')

