FROM postgres:16-alpine

# init scripts die automatisch runnen bij first start (als de data folder leeg is)
COPY init.sql /docker-entrypoint-initdb.d/init.sql
