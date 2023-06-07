import time
import random
from os import path
import yaml
from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily
from prometheus_client import start_http_server
import api

class tls_expiracy(object):
    def __init__(self):
        pass
    def collect(self):
        url_list,result_list = api.check_TLS()
       
        for url in url_list:
            try:
                index = url_list.index(url)
            
                gauge = GaugeMetricFamily(f"{label}", f"target", labels=[f"target"])
                val = int(result_list[index])
                gauge.add_metric([f'{url}'], result_list[index])
                yield gauge
            except:
                print(url+" is unaccessible")
   
if __name__ == "__main__":
    if path.exists('config/config.yml'):
        print("Config file loaded correctly ")
        with open('config/config.yml', 'r') as config_file:
            try:
                config = yaml.safe_load(config_file)
                port = int(config['port'])
                label=config['label']
                frequency = config['scrape_frequency']
               
            except yaml.YAMLError as error:
                print(error)
    start_http_server(port)
    print(f"HTTP server started correctly on port {port}")
    REGISTRY.register(tls_expiracy())
    
    while True: 
        # period between collection
        time.sleep(frequency)