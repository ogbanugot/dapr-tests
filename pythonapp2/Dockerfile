FROM python:3.7-alpine
WORKDIR /app
COPY . /app
RUN rm -rf ./components
RUN pip install requests flask
EXPOSE 3000
ENTRYPOINT ["python"]
CMD ["app.py"]
