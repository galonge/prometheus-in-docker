FROM python:3.6-slim
LABEL maintainer="george@alonge.dev"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["python"]
CMD ["app/app.py"]
