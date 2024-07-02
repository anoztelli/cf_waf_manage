FROM python:3.8-slim-buster

WORKDIR /code

COPY requirements.txt /code/
RUN apt-get update && \
    apt-get install -y gcc && \
    apt-get install -y build-essential

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
