FROM python:3.9.4-buster

# RUN apt update -y && apt install -y gettext # Usado apenas para a geração de traduções
RUN useradd -ms /bin/bash openraffle
USER openraffle

ENV PYTHONUNBUFFERED 1
WORKDIR /home/openraffle/app
ENV PATH $PATH:/home/openraffle/.local/bin

RUN python -m pip install --upgrade pip

COPY ./requirements.txt requirements.txt
RUN --mount=type=cache,target=/home/openraffle/.cache pip install -r requirements.txt debugpy

COPY . .

EXPOSE 8000