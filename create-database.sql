CREATE DATABASE moviescollector;

CREATE USER movies_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE moviescollector TO movies_admin;

