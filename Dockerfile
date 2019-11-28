FROM hypriot/rpi-alpine

RUN apk update && apk add python py-pip

WORKDIR "/exporter"
ADD src .
ADD requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "endpoint.py"]
