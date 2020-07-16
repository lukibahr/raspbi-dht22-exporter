#!/usr/bin/env python
"""
Prometheus running in kubernetes will automatically scrape this service.
"""

import time
import argparse
import logging
import socket
from prometheus_client.core import GaugeMetricFamily, REGISTRY
from prometheus_client import start_http_server
import Adafruit_DHT

SENSOR = Adafruit_DHT.DHT22
LOGFORMAT = "%(asctime)s - %(levelname)s [%(name)s] %(threadName)s %(message)s"

class CustomCollector():
    """
    Class CustomCollector implements the collect function
    """
    def __init__(self, node=None, pin=None, retries=None):
        self.node = node
        self.pin = pin
        self.retries = retries

    def collect(self):
        """collect collects the metrics"""
        humidity, temperature = Adafruit_DHT.read_retry(SENSOR, self.pin, retries=10)
        g = GaugeMetricFamily("temperature_in_celcius", 'Temperature in celcuis', labels=['node'])
        g.add_metric([self.node], temperature)
        yield g

        c = GaugeMetricFamily("humidity_in_percent", 'Humidity in percent', labels=['node'])
        c.add_metric([self.node], humidity)
        yield c

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Prometheus DHT22 sensor exporter')
    parser.add_argument('-n', '--node', type=str, help='The node, the exporter runs on', default=socket.gethostname())
    parser.add_argument('-p', '--port', type=int, help='The port, the exporter runs on', default=9123)
    parser.add_argument('-i', '--interval', type=int, help='The sleep interval of the exporter', default=120)
    parser.add_argument('-r', '--retries', type=int, help='The number of read retries for accurate values', default=6)    
    parser.add_argument('-g', '--gpiopin', type=int, help='The GPIO pin, where the sensor is connected to', default=4)
    parser.add_argument("-l", "--loglevel", choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], help="Set the logging level")
    args = parser.parse_args()
    if args.loglevel:
        logging.basicConfig(level=getattr(logging, args.loglevel), format=LOGFORMAT)
    logging.debug("parsing command line arguments: %s", args)
    logging.info("running exporter on port %s", args.port)
    start_http_server(args.port)
    REGISTRY.register(CustomCollector(args.node, args.gpiopin, args.retries))
    while True:
        logging.debug("pausing %s seconds", args.interval)
        time.sleep(args.interval)
