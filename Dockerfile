FROM hypriot/rpi-alpine:3.6

RUN apk update && apk add python3

WORKDIR "/exporter"
ADD src .
RUN pip3 install Adafruit_DHT --force-pi


ENTRYPOINT ["python3", "exporter.py"]
