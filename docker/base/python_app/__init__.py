import logging
from pyramid.config import Configurator

logger = logging.getLogger(__name__)
def main(global_config, **settings):
    logger.info("Loading Main")
    """ This function returns a Pyramid WSGI application.
    """
    _set_debug(settings)
    with Configurator(settings=settings) as config:
        config.include('pyramid_jinja2')
        config.include('.routes_api', route_prefix="/api")
        config.scan()
    return config.make_wsgi_app()

def _set_debug(settings):
#     import sys
#     sys.path.append('/Applications/Eclipse.app/Contents/Eclipse/plugins/org.python.pydev.core_8.1.0.202012051215/pysrc/pydevd.py')
    import pydevd
    pydevd.settrace('192.168.0.2', port=5678, suspend=False)
    #sys.path.append("")
