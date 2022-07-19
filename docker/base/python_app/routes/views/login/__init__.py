import logging
from pyramid.response import Response

logger = logging.getLogger(__name__)
def includeme(config):
    logger.info("Including route /login")
    config.add_route('login_root', '/login')
    config.scan('.')
