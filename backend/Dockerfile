FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /backend

COPY start.sh requirements.txt /backend/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8000

RUN chmod +x start.sh

CMD ["sh", "start.sh"]
