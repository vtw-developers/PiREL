FROM python:3.9.13
RUN apt-get update && apt-get install -y net-tools iputils-ping htop build-essential
COPY requirements_nopro.txt /root/requirements_nopro.txt
WORKDIR /root
RUN pip install -r requirements_nopro.txt
CMD python