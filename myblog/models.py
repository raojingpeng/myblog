# -*- coding: utf-8 -*-
"""
    :author: raojingpeng
    :github: https://github.com/raojingpeng
    :email: withrjp@gmail.com
"""
from datetime import datetime
from myblog.extensions import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow(), index=True)

    def __repr__(self):
        return '<Post id:%r%r%r%r>' % (self.id, self.title, self.body[1:10], self.timestamp)
