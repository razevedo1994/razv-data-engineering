FROM apache/airflow:2.2.1-python3.9

USER root

COPY ./docker/packages.txt .

RUN if [[ -s packages.txt ]]; then \
    apt-get update && cat packages.txt | xargs apt-get install -y --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*; \
  fi


USER airflow

COPY ./docker/requirements.txt .

RUN if grep -Eqx 'apache-airflow\s*[=~>]{1,2}.*' requirements.txt; then \
    echo >&2 "Do not upgrade by specifying 'apache-airflow' in your requirements.txt, change the base image instead!";  exit 1; \
  fi; \
  pip install --user --no-cache-dir --upgrade pip && \
  pip install --user --no-cache-dir -q -r requirements.txt