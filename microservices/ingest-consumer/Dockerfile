FROM python:3.9-slim as install
FROM install AS base
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    gcc g++ libpq-dev
RUN python -m venv /app/env
ENV PATH="/app/env/bin:$PATH"
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
#####################################
FROM base
ENV PATH="/app/env/bin:$PATH"
COPY app /app
COPY --from=base /app/env /app/env
WORKDIR /app
CMD ["python", "server.py"]