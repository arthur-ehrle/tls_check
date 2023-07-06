# importing the requests library
import re
from os import path
import yaml
from nested_lookup import nested_lookup
import datetime
import time
import OpenSSL
import ssl
import calendar


url_list=[]
port_list = []
result_list=[]


if path.exists('config/config.yml'):
    with open('config/config.yml', 'r') as config_file:
        try:
            config = yaml.safe_load(config_file)
            for URL in config['url_list']:
                url_list.append(URL['link'])
                port_list.append(URL['port'])
        except yaml.YAMLError as error:
            print(error)

def check_TLS(): 
    for url in url_list:
        index = url_list.index(url)
        port = port_list[index]
        try:
            result_list.append(check(url,port)) 
        except:
            pass
    return url_list,result_list

def check(url,port):
    cert=ssl.get_server_certificate((url, port))
    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    bytes=x509.get_notAfter()
    timestamp = bytes.decode('utf-8')

    timestamp= datetime.datetime.strptime(timestamp, '%Y%m%d%H%M%S%z').date().isoformat()
    print(url+":"+timestamp)
    timestamp =calendar.timegm(datetime.datetime.strptime(timestamp, "%Y-%m-%d").timetuple())
    print(timestamp)
    
    return timestamp

