import os


# sqlalchemy
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI','mysql+pymysql://root:root@localhost:3306/demo')
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS',True)


LOG_FILE_PATH = os.environ.get('LOG_FILE_PATH') or 'demo.log'
ERROR_LOG_FILE_PATH = os.environ.get('ERROR_LOG_FILE_PATH') or 'demo.log'