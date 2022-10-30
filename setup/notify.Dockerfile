FROM ubuntu:22.04

ARG DEPENDENCIES="python3-pip"

WORKDIR /srv/utility
COPY ./setup/requirements.txt ./src/notify_changed_ip/*.py ./
RUN apt-get update && \
    apt-get install -y --no-install-recommends ${DEPENDENCIES} && \
    pip3 install --no-cache-dir -r requirements.txt
CMD ["python3", "app.py"]