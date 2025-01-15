FROM python:latest
ARG UID=1000
ARG GID=1000
ARG USERNAME=app
ARG GROUPNAME=app

RUN groupadd -g $GID $GROUPNAME && \
    useradd -m -u $UID -g $GID $USERNAME
COPY --chown=$UID:$GID ./ /usr/src/app
WORKDIR /user/src/app
COPY ./ ./
RUN apt update
RUN pip install --upgrade pip
RUN pip install notion-client
RUN pip install flask
