# -*- coding: utf-8 -*-
"""
    :author: raojingpeng
    :github: https://github.com/raojingpeng
    :email: withrjp@gmail.com
"""
import random
from faker import Faker
from sqlalchemy.exc import IntegrityError

from myblog.extensions import db
from myblog.models import Admin, Category, Post, Comment, Link


fake = Faker()


def fake_admin():
    admin = Admin(
        username='admin',
        blog_title='饶京鹏的博客',
        blog_sub_title='Stay hungry, stay foolish.',
        name='raojingpeng',
        about='withrjp@gmail.com'
    )
    admin.set_password('password')
    db.session.add(admin)
    db.session.commit()


def fake_categories(count=10):
    category = Category(name='Default')
    db.session.add(category)

    for i in range(count):
        category = Category(name=fake.word())
        db.session.add(category)
        # 随机类型可能会重复导致报错
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()


def fake_posts(count=50):
    for i in range(count):
        post = Post(
            title=fake.sentence(nb_words=random.randint(3, 6)),
            body=fake.text(2000),
            category=Category.query.get(random.randint(1, Category.query.count())),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(post)

    db.session.commit()


def fake_comments(count=500):
    for i in range(count):
        comment = Comment(
            author=fake.name(),
            email=fake.email(),
            site=fake.url(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            reviewed=True,
            post=Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(comment)

    # unreviewed comments
    uc = int(count * 0.1)
    for i in range(uc):
        comment = Comment(
            author=fake.name(),
            email=fake.email(),
            site=fake.url(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            reviewed=False,
            post=Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(comment)

        # from admin
        comment = Comment(
            author='raojingpeng',
            email='withrjp@gmail.com',
            site='coming soon..',
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            from_admin=True,
            reviewed=True,
            post=Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(comment)
    db.session.commit()

    # replies
    for i in range(uc):
        comment = Comment(
            author=fake.name(),
            email=fake.email(),
            site=fake.url(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            reviewed=True,
            replied=Comment.query.get(random.randint(1, Comment.query.count())),
            post=Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(comment)
    db.session.commit()


def fake_links():
    baidu = Link(name='百度', url='https://www.baidu.com/')
    weibo = Link(name='新浪微博', url='https://www.weibo.com/')
    stack = Link(name='stack overflow', url='https://stackoverflow.com/')
    github = Link(name='GitHub', url='https://github.com/')
    db.session.add_all([baidu, weibo, stack, github])
    db.session.commit()
