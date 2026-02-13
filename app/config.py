import os

class Config:
    """Base configuration"""
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    ENVIRONMENT = 'development'

class StagingConfig(Config):
    """Staging configuration"""
    ENVIRONMENT = 'staging'

class ProductionConfig(Config):
    """Production configuration"""
    ENVIRONMENT = 'production'

# Config dictionary
config = {
    'development': DevelopmentConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}