# -*- coding: utf-8 -*-
"""
    :author: raojingpeng
    :github: https://github.com/raojingpeng
    :email: withrjp@gmail.com
"""
from flask import Blueprint, render_template, request, current_app

from myblog.extensions import db
from myblog.models import Category, Post


blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['POST_PER_PAGE']
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page, per_page=per_page)
    posts = pagination.items
    categories = Category.query.order_by(Category.id).all()
    return render_template('blog/index.html', pagination=pagination, categories=categories, posts=posts)


@blog_bp.route('/post/<int:post_id>', methods=['GET', 'POST'])
def show_post(post_id):
    page = request.args.get('page', 1)
    per_page = current_app.config['POST_PER_PAGE']
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page, per_page=per_page)
    posts = pagination.items
    categories = Category.query.order_by(Category.id).all()
    return render_template('blog/index.html', pagination=pagination, categories=categories, posts=posts)


@blog_bp.route('/category/<int:category_id>')
def show_category(category_id):
    page = request.args.get('page', 1)
    per_page = current_app.config['POST_PER_PAGE']
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page, per_page=per_page)
    posts = pagination.items
    categories = Category.query.order_by(Category.id).all()
    return render_template('blog/index.html', pagination=pagination, categories=categories, posts=posts)