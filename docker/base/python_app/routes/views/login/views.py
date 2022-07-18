import logging
from pyramid.view import view_config
from pyramid.response import Response
from python_app.routes.views.Views import BaseView

logger = logging.getLogger(__name__)
logger.info("Reading login.view file")

class LoginView(BaseView):
    def __init__(self,request):
        self.request = request


    @view_config(route_name='login_root', request_method='GET', renderer='json')
    def login_root(self):
        logger.info("View login root")
        return Response("OK")