FROM hypriot/rpi-alpine:3.6

RUN apk add python3 gcc python3-dev libc-dev --no-cache

WORKDIR "/exporter"
COPY src .
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "exporter.py"]