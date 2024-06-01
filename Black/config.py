
from decouple import Config

class Config:
    # Configuración para MySQL usando Flask-MySQLdb
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '1607'
    MYSQL_DB = 'black_pumpkin'

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig
}