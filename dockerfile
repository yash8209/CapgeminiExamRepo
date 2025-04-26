FROM python:3.8


WORKDIR /app


RUN apk add --no-cache python3 py3-pip


COPY . /app


RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 5000


CMD ["python", "app.py"]
