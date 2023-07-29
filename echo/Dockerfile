FROM python:3.10-slim

WORKDIR /usr/src/app

COPY requirements.in ./
RUN pip install -r requirements.in
COPY ./ ./

EXPOSE 50051

CMD ["python", "server.py"]
