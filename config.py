import os

USE_REMOTE_DB = os.getenv("USE_REMOTE_DB", "false").lower() == "true"

if USE_REMOTE_DB:
    SQLALCHEMY_DATABASE_URI = os.getenv("REMOTE_DB_URI")
else:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/dashboard_db'

SQLALCHEMY_TRACK_MODIFICATIONS = False
