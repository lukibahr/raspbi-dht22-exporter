# Prometheus exporter for DHT22 Sensors 

Prometheus Endpoint, written in Python to read DHT11 1wire sensor and exposes temperature values as a prometheus metric.

## [TODO]

## Prerequisites

Make sure, you have the required kernel modules loaded. To do so, follow these steps:

```bash
$ sudo modprobe w1-gpio
$ sudo modprobe w1-therm 
$ sudo echo "dtoverlay=w1-gpio" >> /boot/config.txt #to enable 1-wire config and persist after reboot
$ lsmod #check if modules are loaded correctly
$ sudo reboot
```

After your pi has been rebooted, check if you can list the attached 1-wire devices

```bash
$ ls /sys/bus/w1/devices/
```

## Implementation

Have a look at the sourcecode for details. Generally, you'll have to download and import the required python libraries.
Refer to the official documentation on how to implement a prometheus exporter: https://github.com/prometheus/client_python.

### Development

You'll need to install python (I recommend python3) to prepare your local environment: 

```bash
$ sudo apt-get update
$ sudo apt-get install python3-pip
$ sudo python3 -m pip install --upgrade pip setuptools wheel
```

## Dockerrization

I've used hypriot os with a RaspberryPi 3B+. It works on a Raspberry Pi 2 too, although docker builds might take some time, so be calm to your Pi.

## Building and running

You can run the exporter either via python itself or in a docker container. The required commands for running it via python are 
also in the supplied Makefile. For docker use:

```bash
$ docker build -t raspbi-dht22-exporter:arm32v6 -f Dockerfile .
$ docker tag raspbi-dht22-exporter:arm32v6 lukasbahr/raspbi-dht22-exporter:arm32v6
$ docker run -it -e EXPORTER_PORT=9103 -p 9103:9103 raspbi-dht22-exporter:arm32v6
```

You can also download it from docker hub via `docker pull lukasbahr/raspbi-dht22-exporter:arm32v6`

usage: exporter.py [-h] [-n NODE] [-p PORT] [-i INTERVAL] [-g GPIOPIN]
                   [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]

Prometheus DHT22 sensor exporter

optional arguments:
  -h, --help            show this help message and exit
  -n NODE, --node NODE  The node, the exporter runs on
  -p PORT, --port PORT  The port, the exporter runs on
  -i INTERVAL, --interval INTERVAL
                        The sleep interval of the exporter
  -g GPIOPIN, --gpiopin GPIOPIN
                        The GPIO pin, where the sensor is connected to
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --loglevel {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Set the logging level

## Open ToDo's

- [OPEN] Add CI/CD Support. The ci process must detect the underlying system as a raspberry pi in order to install AdafruitDHT22
- [OPEN] Add unit tests
- [OPEN] use buildx to create the proper image
- [OPEN] Add health metric, error metric, scrape interval, general information about exporter etc.