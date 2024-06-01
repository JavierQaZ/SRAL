
from decouple import config

class config:
    # Configuración para MySQL usando Flask-MySQLdb
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root'
    MYSQL_DB = 'black_pumpkin'

class DevelopmentConfig(config):
    DEBUG = True

config = {
    'development': DevelopmentConfig
}