from app.services.postgres import PostgreSQL


class Services:
    postgres: PostgreSQL = PostgreSQL()
    # minio: Minio = Minio()  for example
    # redis: Redis = Redis()  for example
