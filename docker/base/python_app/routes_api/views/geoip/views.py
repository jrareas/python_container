from pyramid.view import view_config
from pyramid.response import Response
from python_app.routes_api.views.Views import BaseAPIView

class GeoipView(BaseAPIView):
    def __init__(self, request):
        self.request = request
    
    @view_config(route_name="geoip_get", request_method="GET", renderer='json')
    def geoip_get(self):
        return "OK"
