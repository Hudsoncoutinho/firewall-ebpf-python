FROM python:3.9-slim

COPY firewall-ebpf.py /firewall-ebpf.py
COPY requirements.txt /requirements.txt

# Instale as dependências
RUN pip install --no-cache-dir -r /requirements.txt

# Defina o comando padrão a ser executado quando o contêiner for iniciado
CMD ["python", "/firewall-ebpf.py"]
