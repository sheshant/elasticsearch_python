import os

HOST = os.environ.get("ES_HOST_NAME", "https://localhost:9200")
USERNAME = os.environ.get("ES_USERNAME", "elastic")
PASSWORD = os.environ.get("ES_PASSWORD", "supersecurepassword")

DATABASE_NAME = os.environ.get("DATABASE_NAME", "kafka_database")
DATABASE_USER = os.environ.get("DATABASE_USER", "test_user")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD", "rootuser")
DATABASE_HOST = os.environ.get("DATABASE_HOST", "")
DATABASE_PORT = os.environ.get("DATABASE_PORT", "")
