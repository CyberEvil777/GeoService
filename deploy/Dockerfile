FROM python:3.8-slim

ENV PROJECT_ROOT /project/
ENV SRC_DIR /src
ENV DEPLOY_DIR ./deploy
ENV GUNICORN_CONF $PROJECT_ROOT/gunicorn.conf.py


RUN apt update
RUN apt install -y gdal-bin gcc


RUN pip install --upgrade pip wheel pipenv

COPY  ./$SRC_DIR/Pipfile $PROJECT_ROOT
COPY ./$SRC_DIR/Pipfile.lock $PROJECT_ROOT
COPY ./deploy/gunicorn.conf.py $GUNICORN_CONF

WORKDIR $PROJECT_ROOT

RUN pipenv install --deploy --system

COPY ./$SRC_DIR $PROJECT_ROOT



COPY ./$DEPLOY_DIR/run_django.sh $PROJECT_ROOT

RUN chmod +x $PROJECT_ROOT/run_django.sh
CMD ["/project/run_django.sh"]
