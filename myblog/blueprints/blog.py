# -*- coding: utf-8 -*-
"""
    :author: raojingpeng
    :github: https://github.com/raojingpeng
    :email: withrjp@gmail.com
"""
from flask import Blueprint


blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/')
def index():
    return '<h1>Hello World!</h1>'
