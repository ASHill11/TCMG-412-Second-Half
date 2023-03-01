# 1. Base image
FROM python:3.9

# These statements should set our current working directory as the place to be
WORKDIR /TCMG-412-Second-Half
COPY . /TCMG-412-Second-Half/requirements.txt

RUN pip install -r requirements.txt

CMD ["python", "API.py"]
