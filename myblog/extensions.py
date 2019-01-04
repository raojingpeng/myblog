# -*- coding: utf-8 -*-
"""
    :author: raojingpeng
    :github: https://github.com/raojingpeng
    :email: withrjp@gmail.com
"""
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment

login_manager = LoginManager()
db = SQLAlchemy()
csrf = CSRFProtect()
mail = Mail()
bootstrap = Bootstrap()
moment = Moment()
