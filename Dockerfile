# To build api locally:
# docker build . -t g0-api

# To pull image from dockerhub
# docker image pull ashill11/tcmg-412-api:g0-api

# To run container
# docker run -p 4000:4000 --rm ashill11/tcmg-412-api:g0-api
# Make sure you visit the localhost on port 8000

# You will probably need to kill the container from another command line

# 1. Base image
FROM python:3.9

# These statements should set our current working directory as the place to be
WORKDIR /TCMG-412-Second-Half
COPY . /TCMG-412-Second-Half

RUN pip install -r requirements.txt

CMD ["python", "API.py"]
