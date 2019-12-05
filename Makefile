# Makefile

RUNPYTHON = $(shell which python)
RUNLINT = $(shell which pylint)
RUNPIP = $(shell which pip)
RUNDOCKER = $(shell which docker) 

IMAGE = lukasbahr/raspbi-dht22-exporter
VERSION = master

EXPORTER_PORT=8888

all: requirements lint run
 
lint: 
	$(RUNLINT) $(PWD)/src/exporter.py

requirements:
	$(RUNPIP) install -r requirements.txt --user

run: 
	$(RUNPYTHON) src/endpoint.py

login:
	$(RUNDOCKER) login -u $(DOCKERHUB_USER) -p $(DOCKERHUB_PASSWORD)

build:
	$(RUNDOCKER) $(@) -t $(IMAGE):$(VERSION) -f Dockerfile .

tag:
	$(RUNDOCKER) $(@) $(IMAGE):$(VERSION) $(IMAGE):$(VERSION)

push:
	$(RUNDOCKER) $(@) $(IMAGE):$(VERSION)