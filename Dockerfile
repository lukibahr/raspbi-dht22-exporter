FROM python:3.7-alpine3.9

RUN apk update && apk add python py-pip

WORKDIR "/exporter"
ADD src .
ADD requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "endpoint.py"]
