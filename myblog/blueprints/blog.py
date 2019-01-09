# -*- coding: utf-8 -*-
"""
    :author: raojingpeng
    :github: https://github.com/raojingpeng
    :email: withrjp@gmail.com
"""
from flask import Blueprint, render_template

from myblog.extensions import db
from myblog.models import Post


blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/')
def index():
    title = 'test'
    body = 'hahaha'
    post = Post(title=title, body=body)
    db.session.add(post)
    db.session.commit()
    return render_template('blog/index.html')
