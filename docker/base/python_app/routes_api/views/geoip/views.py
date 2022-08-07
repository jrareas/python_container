from pyramid.view import view_config
from pyramid.response import Response
from python_app.routes_api.views.Views import BaseAPIView
from python_app.routes_api.views.geoip.geoip_class import GeoIP
import os 
import geoip2.database


class GeoipView(BaseAPIView):
    def __init__(self, request):
        self.request = request
    
    @view_config(route_name="geoip_get", request_method="GET", renderer='json')
    def geoip_get(self):
        ip = self.request.params['ip']
        geoip = GeoIP()
        city_name = geoip.get_city_name(ip)
        return city_name
    
