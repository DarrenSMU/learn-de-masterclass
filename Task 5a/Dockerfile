FROM postgres
ENV POSTGRES_DB db
COPY 01-postgres-sakila-schema.sql /docker-entrypoint-initdb.d/
COPY 02-postgres-sakila-insert-data.sql /docker-entrypoint-initdb.d/
