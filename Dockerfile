FROM python
WORKDIR /opt/
ADD . .
RUN python setup.py install
RUN chmod +x iofga.py
ENTRYPOINT ["python","iofga.py"]
