import os


class DevConfig():

    DEBUG = 1
    SQLALCHEMY_TRACK_MODIFICATIONS = 0
    path = os.path.join(os.getcwd(), 'rmon.db').replace('\\', '/') # 目的是把\\换成/，否则在windows下这种路径是非法的
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(path)
    TEMPLATES_AUTO_RELOAD = 1
    


class ProductConfig(DevConfig):

    DEBUG = 0
    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/shiyanlou'
    
    


