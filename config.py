import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    FLASK_APP = os.getenv('FLASK_APP', 'app.py')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///dev.db')

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', '1') == '1'

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    FLASK_DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
