import logging
from python_app.routes.views.login.views import LoginView 
from pyramid.response import Response

logger = logging.getLogger(__name__)
def includeme(config):
    logger.info("Including route /login")
    config.add_route('login_root', '/login')
    config.scan('.')


def view_func(request):
    return Response('OK')