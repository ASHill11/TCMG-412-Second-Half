# HOW TO RUN:
# NOTE - Use terminal within your virtual environment
# On first time run the following:
# docker build . -t g0-api
# Then, run the following:
# docker run -p 8000:4000 g0-api
# Make sure you visit the localhost on port 8000

# 1. Base image
FROM python:3.9

# These statements should set our current working directory as the place to be
WORKDIR /TCMG-412-Second-Half
COPY . /TCMG-412-Second-Half

RUN pip install -r requirements.txt

CMD ["python", "API.py"]
