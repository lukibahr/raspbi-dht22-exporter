# Prometheus exporter for DHT22 Sensors 

<<<<<<< HEAD
[![Build Status](https://ci.devopoly.de/api/badges/lukibahr/raspbi-temperature-exporter/status.svg)](https://ci.devopoly.de/lukibahr/raspbi-temperature-exporter) [![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/) [![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)



Prometheus Endpoint, written in Python to read DHT11 1wire sensor and exposes temperature values as a prometheus metric.
=======
Prometheus Endpoint, written in Python to read DHT22 1wire sensor and exposes temperature values as a prometheus metric.
>>>>>>> 100a4f5f6bdefd9ef07d875f67c2146c95e0b092

## Prerequisites - Wiring the sensor

t.b.d.

## Implementation

Have a look at the sourcecode for details. Generally, you'll have to download and import the required python libraries.
Refer to the official documentation on how to implement a prometheus exporter: https://github.com/prometheus/client_python.

### Development

You'll need to install python (I recommend python3) to prepare your local environment: 

```bash
$ sudo apt-get update
$ sudo apt-get install python3-pip
$ sudo python3 -m pip install --upgrade pip setuptools wheel
$ sudo pip3 install prometheus_client Adafruit_DHT
$ python3 exporter.py --< args[] >
```

## Running in docker

I've used hypriot os with a RaspberryPi 3B+. It works on a Raspberry Pi 2 too, although docker builds might take some time, so be calm to your Pi.

```bash
python3 src/exporter.py --help
usage: exporter.py [-h] [-n NODE] [-p PORT] [-i INTERVAL] [-r RETRIES]
                   [-g GPIOPIN] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]

Prometheus DHT22 sensor exporter

optional arguments:
  -h, --help            show this help message and exit
  -n NODE, --node NODE  The node, the exporter runs on
  -p PORT, --port PORT  The port, the exporter runs on
  -i INTERVAL, --interval INTERVAL
                        The sleep interval of the exporter
  -r RETRIES, --retries RETRIES
                        The number of read retries for accurate values
  -g GPIOPIN, --gpiopin GPIOPIN
                        The GPIO pin, where the sensor is connected to
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --loglevel {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Set the logging level
```

A sample local run can be the following: `python3 exporter.py --node=localhost --port=9103 --interval=10 --gpiopin=4 --loglevel=DEBUG`

## Building and running

You can run the exporter either via python itself or in a docker container. The required commands for running it via python are 
also in the supplied Makefile. For docker use:

```bash
$ docker build -t lukasbahr/raspbi-dht22-exporter:<VERSION> -f Dockerfile .
$ docker tag lukasbahr/raspbi-dht22-exporter:<VERSION> lukasbahr/raspbi-dht22-exporter:<VERSION>
$ docker run -it -p 9103:9103 lukasbahr/raspbi-dht22-exporter:<VERSION>
```

or refer to the supplied Makefile.

You can also download it from docker hub via `docker pull lukasbahr/raspbi-dht22-exporter:<VERSION>`

## Open ToDo's

- :x: Add CI/CD Support. The ci process must detect the underlying system as a raspberry pi in order to install AdafruitDHT22
- :x: Add unit tests
- :x: use buildx to create the proper image
- :x: Add health metric, error metric, scrape interval, general information about exporter etc.
- :x: move to [Adafruit_CircuitPython_DHT](https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/python-setup)
- :x: Fix docs for docker-compose and docker run 

## Troubleshooting

DHT22 sensors are hard to read. If your scrape interval is too high, you might encounter the following error. This error indicates that the socket connection has been closed before the client did. Increase your scrape interval to 60 or 120 seconds - we all hope, that the temperature does not rapidly change its value within this time.

```bash
dht22-exporter-4zzlm dht22-exporter ----------------------------------------
dht22-exporter-4zzlm dht22-exporter Exception happened during processing of request from ('10.42.2.74', 36426)
dht22-exporter-4zzlm dht22-exporter Traceback (most recent call last):
dht22-exporter-4zzlm dht22-exporter   File "/usr/lib/python3.6/socketserver.py", line 654, in process_request_thread
dht22-exporter-4zzlm dht22-exporter     self.finish_request(request, client_address)
dht22-exporter-4zzlm dht22-exporter   File "/usr/lib/python3.6/socketserver.py", line 364, in finish_request
dht22-exporter-4zzlm dht22-exporter     self.RequestHandlerClass(request, client_address, self)
dht22-exporter-4zzlm dht22-exporter   File "/usr/lib/python3.6/socketserver.py", line 724, in __init__
dht22-exporter-4zzlm dht22-exporter     self.handle()
dht22-exporter-4zzlm dht22-exporter   File "/usr/lib/python3.6/http/server.py", line 418, in handle
dht22-exporter-4zzlm dht22-exporter     self.handle_one_request()
dht22-exporter-4zzlm dht22-exporter   File "/usr/lib/python3.6/http/server.py", line 406, in handle_one_request
dht22-exporter-4zzlm dht22-exporter     method()
dht22-exporter-4zzlm dht22-exporter   File "/usr/lib/python3.6/site-packages/prometheus_client/exposition.py", line 159, in do_GET
dht22-exporter-4zzlm dht22-exporter     self.wfile.write(output)
dht22-exporter-4zzlm dht22-exporter   File "/usr/lib/python3.6/socketserver.py", line 803, in write
dht22-exporter-4zzlm dht22-exporter     self._sock.sendall(b)
dht22-exporter-4zzlm dht22-exporter BrokenPipeError: [Errno 32] Broken pipe
```

## Further reading

- https://pinout.xyz/pinout/pin7_gpio4
