FROM python:3.7-alpine
MAINTAINER omotundetolu@gmail.com
WORKDIR /code
ENV FLASK_APP app.py
# ENV FLASK_RUN_HOST 0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
RUN cp -a src/* tests
RUN ["pytest", "-v", "--junitxml=reports/result.xml"]
ENTRYPOINT ["python"]
CMD ["src/app.py"]
