FROM python:3.9-slim

COPY firewall-ebpf.py /firewall-ebpf.py
COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r /requirements.txt


CMD ["python", "/firewall-ebpf.py"]
