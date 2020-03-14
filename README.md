# Prometheus exporter for DHT22 Sensors 

Prometheus Endpoint, written in Python to read DHT11 1wire sensor and exposes temperature values as a prometheus metric.

## Prerequisites - Wiring the sensor

t.b.d.


```bash
$ sudo modprobe w1-gpio
$ sudo modprobe w1-therm 
$ sudo echo "dtoverlay=w1-gpio" >> /boot/config.txt #to enable 1-wire config and persist after reboot
$ lsmod #check if modules are loaded correctly
$ sudo reboot
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
$ sudo pip3 install prometheus_client Adafruit_DHT
$ python3 exporter.py --< args[] >
```

## Running in docker

I've used hypriot os with a RaspberryPi 3B+. It works on a Raspberry Pi 2 too, although docker builds might take some time, so be calm to your Pi.

```bash
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
```

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

## Further reading

- https://pinout.xyz/pinout/pin7_gpio4