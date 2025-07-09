
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
EXPOSE 4449
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=4449"]
