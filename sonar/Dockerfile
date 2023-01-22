FROM ubuntu:20.04

RUN apt update
RUN apt install -y python3 python3-pip
RUN pip install streamlit
RUN pip install tensorflow
RUN pip install scikit-learn
RUN pip install sklearn
RUN pip install pandas
RUN pip install numpy

EXPOSE 8501

COPY . /root/sonar


WORKDIR /root/sonar
RUN chmod +x /root/sonar/file_run.sh

ENTRYPOINT [ "/root/sonar/file_run.sh","--server.port=8501", "--server.address=0.0.0.0" ]