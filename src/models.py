import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    posts = relationship('Post', backref='user', lazy=True)
    comments = relationship('Comment', backref='user', lazy=True)


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)
    comments = relationship('Comment', backref='post', lazy=True)
    tagmaps = relationship('Tagmap', backref='post', lazy=True)

    def to_dict(self):
        return {}


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    content = Column(String(100), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    post = relationship(Post)

    def to_dict(self):
        return {}


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    tagmaps = relationship('Tagmap', backref='tag', lazy=True)

    def to_dict(self):
        return {}


class Tagmap(Base):
    __tablename__ = 'tagmap'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    post = relationship(Post)
    tag_id = Column(Integer, ForeignKey('tag.id'), nullable=False)
    tag = relationship(Tag)

    def to_dict(self):
        return {}


# Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
