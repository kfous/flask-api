FROM python:3.9

WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip
RUN pip install virtualenv
RUN virtualenv venv

RUN . venv/bin/activate && pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV MONGO_URI=mongodb://mongo:27017/sentiment_db

CMD ["flask", "run", "--host=0.0.0.0"]
