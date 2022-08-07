import os 
import geoip2.database
class GeoIP():
    def get_response(self,ip):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        print(__file__)
        db_file = os.path.join(dir_path,'GeoLite2-City.mmdb')
        print (db_file)
        with geoip2.database.Reader(db_file)as reader:
            response = reader.city(ip)
        return response
    
    def get_city_name (self,ip):
        response = self.get_response (ip) 
        return response.city.name

    def get_country_name (self,ip):
        response = self.get_response(ip)
        return response.country.name

    def get_postal_code (self,ip):
        response = self.get_response(ip)
        return response.postal.code
    
    def get_latitude (self,ip):
        response = self.get_response(ip)
        return response.location.latitude

    def get_longitude (self,ip):
        response = self.get_response(ip)
        return response.location.longitude
    