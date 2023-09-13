FROM python:3-alpine3.18
WORKDIR /POE-Api-Project
COPY . /POE-Api-Project/
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./path-of-exile-builds-API.py