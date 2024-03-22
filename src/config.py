from environs import Env

env = Env()
env.read_env()

SECRET_KEY = env.str("SECRET_KEY")

PG_DB_NAME = env("PG_DB_NAME")
PG_USER = env("PG_USER")
PG_PASS = env("PG_PASS")
PG_HOST = env("PG_HOST")
PG_PORT = env.int("PG_PORT")

# Redis
REDIS_HOST = env("REDIS_HOST")
REDIS_PORT = env.int("REDIS_PORT")