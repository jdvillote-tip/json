from requests import get

loc = get('https://ipapi.co/json/')
ip_info = loc.json()

ip_add = ip_info['ip']
ip_loc = ip_info['country_name']
ip_lat = ip_info['latitude']
ip_long = ip_info['longitude']
ip_region = ip_info['region']
ip_asn = ip_info['asn']
ip_cc = ip_info['country_code']

print(ip_add)
print(ip_region)
print(ip_lat)
print(ip_long)
print(ip_loc)
print(ip_cc)
print(ip_asn) 
import requests

#Class for Getting the IP Address Information of the User
class Own_IP_Address:

    #Initialization of API to get Public IP Address of the User
    def __init__(self):
        self.main_url = 'https://ipapi.co/json/'
        self.loc = requests.get(self.main_url)
        self.ip_info = self.loc.json()

    #Get the Public IP Address of the User
    def get_ip(self):

        #Getting the IP Address and it's version
        self.public_ip = self.ip_info['ip']
        self.public_ip_type = self.ip_info['version']

        #Display of IP Address Information
        print("*--------------- Personal IP Address ----------------*")
        print(f"IP Address: {self.public_ip}")
        print(f"IP Address Version: {self.public_ip_type}")
        print("*----------------------------------------------------*")

    #Get the Geological Location of the User
    def get_geological_info(self):

        #Getting the Information of the Location
        self.ip_loc_country_code = self.ip_info['country_code']
        self.ip_loc_country = self.ip_info['country_name']
        self.ip_loc_region = self.ip_info['region']
        self.ip_loc_latitute = self.ip_info['latitude']
        self.ip_loc_longitude = self.ip_info['longitude']

        #Display of User Location based on IP Address
        print("*------------------ User Location -------------------*")
        print(f"Country Code: {self.ip_loc_country_code}")
        print(f"Country Name: {self.ip_loc_country}")
        print(f"Region: {self.ip_loc_region}")
        print(f"Latitude: {self.ip_loc_latitute}")
        print(f"Longitude: {self.ip_loc_longitude}")
        print("*----------------------------------------------------*")

    #Getting the ISP and ASN of the User IP Address
    def get_isp_info(self):
        #Getting the ISP and ASN
        self.ip_isp = self.ip_info['org']
        self.ip_asn = self.ip_info['asn']

        #Display of ISP and ASN of User
        print("*--------------- User ISP Information ---------------*")
        print(f"Internet Service Provider: {self.ip_isp}")
        print(f"Autonomous System Number: {self.ip_asn}")
        print("*----------------------------------------------------*")

home_device = Own_IP_Address()
home_device.get_ip()
home_device.get_geological_info()
home_device.get_isp_info()