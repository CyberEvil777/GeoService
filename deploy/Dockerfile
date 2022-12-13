FROM python:3.8-slim

ENV PROJECT_ROOT /project
ENV SRC_DIR /src
ENV DEPLOY_DIR ./deploy
# ENV RUN_DJANGO $PROJECT_ROOT/run_django.sh

RUN mkdir $PROJECT_ROOT
RUN mkdir $SRC_DIR
RUN echo $PROJECT_ROOT
RUN dir $SRC_DIR
# COPY $DEPLOY_DIR/gunicorn.conf.py $PROJECT_ROOT
# COPY $DEPLOY_DIR/run_django.sh $PROJECT_ROOT


# COPY $DEPLOY_DIR/run_django.sh $PROJECT_ROOT

RUN pip install --upgrade pip wheel pipenv

# COPY ./src/Pipfile $SRC_DIR
# COPY ./src/Pipfile.lock $SRC_DIR
COPY  ./GeoService$SRC_DIR/Pipfile $PROJECT_ROOT
COPY ./$SRC_DIR/Pipfile.lock $PROJECT_ROOT
# COPY Pipfile .
# COPY Pipfile.lock .
# RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy


WORKDIR $PROJECT_ROOT
RUN pipenv install

# COPY ./$SRC_DIR $PROJECT_ROOT

RUN chmod +x $PROJECT_ROOT/run_django.sh
CMD ["/project/run_django.sh"]
