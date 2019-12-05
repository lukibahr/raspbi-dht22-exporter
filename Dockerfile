FROM hypriot/rpi-alpine:3.6

RUN apk update && apk add python3 gcc python3-dev libc-dev

WORKDIR "/exporter"
ADD src .
RUN pip3 install prometheus_client Adafruit_DHT

ENTRYPOINT ["python3", "exporter.py"]