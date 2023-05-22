from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import pymysql
from Config.config import config

db = SQLAlchemy()
cors = CORS()


def create_app(config_name):
    # print(Config[config_name].SQLALCHEMY_DATABASE_URI)
    app = Flask(__name__)
    # 导入配置文件
    app.config.from_object(config[config_name])
    # 配置文件注册到app
    config[config_name].init_app(app)

    db.init_app(app)
    cors.init_app(app)

    import app.user.views as user
    app.register_blueprint(user.bp)
    import app.run.views as run
    app.register_blueprint(run.bp)
    import app.admin.views as admin
    app.register_blueprint(admin.bp)
    import app.activity.views as activity
    app.register_blueprint(activity.bp)

    # 注册数据库模型
    from app.user import models
    from app.run import models
    from app.activity import models

    return app


pymysql.install_as_MySQLdb()

