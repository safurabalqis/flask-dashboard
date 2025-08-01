import os

USE_REMOTE_DB = os.getenv("USE_REMOTE_DB", "false").lower() == "true"

if USE_REMOTE_DB:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://sql12793151:VWpIPv78A8@sql12.freesqldatabase.com:3306/sql12793151'
else:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/dashboard_db'

SQLALCHEMY_TRACK_MODIFICATIONS = False
