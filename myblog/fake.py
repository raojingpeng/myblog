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
from myblog.models import Admin, Category, Post


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
            title=fake.sentence(),
            body=fake.text(2000),
            category=Category.query.get(random.randint(1, Category.query.count())),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(post)

    db.session.commit()
