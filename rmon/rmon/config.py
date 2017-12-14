import os


class DevConfig():

    DEBUG = 1
    SQLALCHEMY_TRACK_MODIFICATIONS = 0
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    TEMPLATES_AUTO_RELOAD = 1


class ProductConfig(DevConfig):

    DEBUG = 0

    path = os.path.join(os.getcwd(), 'rmon.db').replace('\\', '/')

    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(path)


