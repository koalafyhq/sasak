class Config(object):
    DEBUG = False
    TESTING = False
    MAX_SIZE_IN_MB = 10
    SECRET_KEY = "rahasia"

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    MAX_SIZE_IN_MB = 2
    TESTING = True
