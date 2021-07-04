FROM python:3.9.5-slim

RUN python -c "import urllib.request as req; req.urlretrieve('https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip', 'awscliv2.zip')" && \
  unzip awscliv2.zip && ./aws/install

RUN pip install -U pip wheel && pip install locust boto3 pyyaml

RUN echo >> /etc/security/limits.conf && \
    echo "locust  soft  nofile 50000" >> /etc/security/limits.conf && \
    echo "locust  hard  nofile 50000" >> /etc/security/limits.conf && \
    echo "fs.file-max=500000" > /etc/sysctl.d/local.conf

WORKDIR /locust
COPY entrypoint.py .
RUN chmod +x entrypoint.py
ENTRYPOINT ["./entrypoint.sh"]

# turn off python output buffering
ENV PYTHONUNBUFFERED=1
