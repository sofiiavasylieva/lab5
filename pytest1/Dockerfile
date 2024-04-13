FROM python:3.10-bullseye

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# set work directory
WORKDIR /app

# copy project
COPY . /app

# upgrade pip
RUN /opt/venv/bin/python -m pip install --upgrade pip --no-cache-dir setuptools wheel pip-tools
RUN pip install psycopg2-binary

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
# COPY requirements.in .
RUN pip install -r requirements/requirements.txt


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]