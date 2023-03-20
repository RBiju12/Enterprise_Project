FROM ubuntu:18.04
RUN apt-get update && apt-get -y install python
RUN apt-get install python3-pip -y
RUN pip install flask 
COPY . /opt
EXPOSE 5000
CMD ["python3", "/opt/app.py"]
