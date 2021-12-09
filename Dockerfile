# set base image (host OS)
FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
WORKDIR /app
CMD ["python", "main.py"]