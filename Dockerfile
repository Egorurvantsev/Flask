FROM python:3.10-buster

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]