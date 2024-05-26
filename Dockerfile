FROM python:3.9

WORKDIR /app

COPY app.py .
COPY clean_data.py .
COPY requirements.txt .
COPY setup_the_db.py .

# RUN sudo apt-get update

# RUN sudo apt install build-essential

RUN pip install -r requirements.txt

COPY start.sh .

RUN chmod +x start.sh

CMD ["./start.sh"]