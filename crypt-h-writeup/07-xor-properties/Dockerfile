FROM python:3.8

WORKDIR /my-env

COPY sol.py .

RUN pip install pwntools

ENTRYPOINT ["/usr/local/bin/python3"]
CMD ["./sol.py"]