# tls_check
Simple tool to get the expiration date of TLS certificate and expose it to Prometheus.

# Docker
Link to the docker image : https://hub.docker.com/r/aehr/tls_check.

# Utilisation
Exporter is exposing metrics at : http://localhost:PortNumber/
You can change the port in the YAML file. You will have to mount the config file on the container in /app/config/  .
There is some metrics about the python process itslef, but the most importants metrics are tagged by "TLS_expiration_date" at the begining.
You can add other urls that you will want to monitor by putting the associated port. 

# config.yml
port: 7790
scrape_frequency: 1 \
label : "TLS_expiration_date" \
url_list : 
  - link : "github.com" \
    port : 443
 


