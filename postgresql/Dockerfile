FROM postgres

RUN mkdir /var/lib/PostgresConfig

COPY init.sql /docker-entrypoint-initdb.d/init.sql
COPY config/ /var/lib/PostgresConfig/

WORKDIR /var/lib/postgresql

EXPOSE $SQL_DB_PORT

CMD [\
  "postgres", \
  "-c", \
  "config_file=/var/lib/PostgresConfig/postgresql.conf"\
]
