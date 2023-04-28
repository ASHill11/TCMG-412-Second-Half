
# To build api locally:
# docker build . -t g0-api

# To pull image from dockerhub
# docker image pull ashill11/tcmg-412-api:g0-api

# To run container
# docker run -p 4000:4000 --rm ashill11/tcmg-412-api:g0-api
# Make sure you visit the localhost on port 8000

# You will probably need to kill the container from another command line

# 1. Base image
FROM python:3.8.1-alpine3.11

# These statements should set our current working directory as the place to be
WORKDIR /TCMG-412-Second-Half
COPY . /TCMG-412-Second-Half

RUN apk add --no-cache git
RUN pip install -r requirements.txt
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
EXPOSE 5000
COPY requirements.txt requirements.txt
CMD ["flask", "run"]
CMD ["python", "API.py"]
