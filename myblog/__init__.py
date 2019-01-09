# -*- coding: utf-8 -*-
"""
    :author: raojingpeng
    :github: https://github.com/raojingpeng
    :email: withrjp@gmail.com
"""
import os
from flask import Flask

from myblog.blueprints.admin import admin_bp
from myblog.blueprints.auth import auth_bp
from myblog.blueprints.blog import blog_bp
from myblog.extensions import login_manager, db, csrf, mail, bootstrap, moment
from myblog.settings import config


def create_app(config_name=None):
    """Factory Function"""
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('myblog')
    app.config.from_object(config[config_name])

    register_extensions(app)
    register_blueprints(app)
    register_shell_context(app)

    return app


def register_extensions(app):
    login_manager.init_app(app)
    db.init_app(app)
    csrf.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)


def register_blueprints(app):
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(blog_bp)


def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db)
