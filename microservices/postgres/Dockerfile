ARG PGVERSION=${PGVERSION:-13}
ARG POSTGIS_VERSION=${POSTGIS_VERSION:-3}
FROM postgres:${PGVERSION}

ARG PGVERSION
ARG POSTGIS_VERSION

ENV PGVERSION $PGVERSION
ENV POSTGIS_VERSION $POSTGIS_VERSION

RUN apt-get update && apt-get install -y postgis postgresql-13-postgis-3 postgresql-contrib-13

# All Credits go to https://github.com/postgis/docker-postgis
RUN mkdir -p /docker-entrypoint-initdb.d
COPY ./initdb-postgis.sh /docker-entrypoint-initdb.d/10_postgis.sh
COPY ./update-postgis.sh /usr/local/bin
