FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
EXPOSE 8000
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /app/
# CMD ["uvicorn", "api.api:app", "--host 0.0.0.0"]