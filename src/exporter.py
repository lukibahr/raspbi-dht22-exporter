#!/usr/bin/env python
"""
Prometheus running in kubernetes will automatically scrape this service.
"""
import os
import logging
from prometheus_client import start_http_server, Gauge
from w1thermsensor import W1ThermSensor

# Create a metric to track time spent and requests made.
G = Gauge('temp_in_celcius', 'Temperature in celcuis', ['sensor'])
SENSOR = W1ThermSensor()
LOGFORMAT = "%(asctime)s - %(levelname)s [%(name)s] %(threadName)s %(message)s"
logging.basicConfig(level=logging.INFO, format=LOGFORMAT)

def process_temperature():
    """ a function to process the temperature """
    
    """for mutliple Sensors"""

    for SENSOR in W1ThermSensor.get_available_sensors():
	logging.info("Sensor %s has temperature %.2f" % (SENSOR.id, SENSOR.get_temperature()))
     	G.labels("%s" % SENSOR.id).set("%.2f" % SENSOR.get_temperature())


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    if 'EXPORTER_PORT' in os.environ:  
        
        logging.info("Running exporter on port: %s", os.getenv('EXPORTER_PORT'))
        start_http_server(int(os.getenv('EXPORTER_PORT')))
        # call process temperature function
        while True:
            process_temperature()
    else:
        logging.error("EXPORTER_PORT variable is not set.")