FROM python:3.11.0-alpine
COPY . /app
WORKDIR /app
RUN python -m dotenv SAMIE
RUN SAMIE/Scripts/activate
RUN pip install -r requirements.txt
RUN flask --app app run --debug
ENTRYPOINT ["python"]
CMD ["app.py"]

EXPOSE 80
USER 10014
