FROM python:3.10-slim

WORKDIR /usr/src/app

RUN pip install flask
COPY ./ ./

EXPOSE 5000

CMD ["flask", "--app=server", "run", "--host=0.0.0.0"]
