# 配置文件

import os
# from flask import load_dotenv 将导致错误
from flask.cli import load_dotenv


class Config:
    # 加载环境配置文件
    load_dotenv('.flaskenv')

    # 禁用修改跟踪系统
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 请求结束时自动提交数据库数据
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL')


class ProductionConfig(Config):
    # 生产环境中不能使用调试
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
