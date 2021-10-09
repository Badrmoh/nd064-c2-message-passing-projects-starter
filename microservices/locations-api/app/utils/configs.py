from os import environ

# Configurations
messages: list = []
KAFKA_TOPIC = str(environ.get('KAFKA_TOPIC', 'locations'))
KAFKA_SERVICE = str(environ.get('KAFKA_SERVICE'))
SERVER_PORT = str(environ.get('SERVER_PORT', '[::]:5005'))
MAX_WORKERS = int(environ.get('MAX_WORKERS', 2))
DB_USERNAME = environ.get("DB_USERNAME")
DB_PASSWORD = environ.get("DB_PASSWORD")
DB_HOST = environ.get("DB_HOST")
DB_PORT = environ.get("DB_PORT")
DB_NAME = environ.get("DB_NAME")