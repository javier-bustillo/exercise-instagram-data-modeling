import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, UnicodeText, DateTime
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


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False )
    content = Column(UnicodeText, nullable=False) 
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)

    def to_dict(self):
        return {}


# Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
