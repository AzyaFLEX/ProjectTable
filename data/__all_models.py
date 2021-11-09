from sqlalchemy import Column, Integer, Text, DateTime, String, Boolean, ForeignKey
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase
from flask_login import UserMixin


class Event(UserMixin, SqlAlchemyBase, SerializerMixin):
	__tablename__ = "events"
	id = Column(Integer, primary_key=True, autoincrement=True)
	datetime = Column(DateTime)
	text = Column(String)


class Message(UserMixin, SqlAlchemyBase, SerializerMixin):
	__tablename__ = "messages"
	id = Column(Integer, primary_key=True, autoincrement=True)
	sender = Column(Integer)
	receiver = Column(Integer)
	text = Column(String)
	datetime = Column(DateTime)
	is_read = Column(Boolean, default=False)


class User(UserMixin, SqlAlchemyBase, SerializerMixin):
	__tablename__ = "users"
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String, unique=True)
	email = Column(String, unique=True)
	password = Column(String)
	description = Column(Text, default="")


class Post(UserMixin, SqlAlchemyBase, SerializerMixin):
	__tablename__ = "posts"
	id = Column(Integer, primary_key=True, autoincrement=True)
	author = Column(Integer, ForeignKey('users.id'))
	text = Column(Text, default='')
	turn_off_comments = Column(Boolean, default=False)
	anonymous = Column(Boolean)
	datetime = Column(DateTime)
	comments = Column(String, default="")
	likes = Column(Integer, default=0)


class QAA(UserMixin, SqlAlchemyBase, SerializerMixin):
	__tablename__ = "qaa"
	id = Column(Integer, primary_key=True, autoincrement=True)
	title = Column(String)
	author = Column(Integer, ForeignKey('users.id'))
	text = Column(Text, default='')
	anonymous = Column(Boolean)
	datetime = Column(DateTime)
	rating = Column(Integer, default=0)
	rated = Column(Integer, default=0)
	tags = Column(String, default="")
	answers = Column(Integer, default=0)
	answered = Column(Boolean, default=False)
	views = Column(Integer, default=0)


class Answer(UserMixin, SqlAlchemyBase, SerializerMixin):
	__tablename__ = "answ"
	id = Column(Integer, primary_key=True, autoincrement=True)
	qaa_id = Column(Integer, ForeignKey('qaa.id'))
	author = Column(Integer, ForeignKey('users.id'))
	text = Column(Text, default='')
	datetime = Column(DateTime)
	likes = Column(Integer, default=0)


class File(UserMixin, SqlAlchemyBase, SerializerMixin):
	__tablename__ = "files"
	id = Column(Integer, primary_key=True, autoincrement=True)
	way = Column(String)
	type = Column(String)
	author = Column(Integer, ForeignKey('users.id'))
	post_id = Column(Integer, ForeignKey('posts.id'))


class Comment(UserMixin, SqlAlchemyBase, SerializerMixin):
	__tablename__ = "comments"
	id = Column(Integer, primary_key=True, autoincrement=True)
	text = Column(String)
	author = Column(Integer, ForeignKey('users.id'))
	likes = Column(Integer, default=0)
	post_id = Column(Integer, ForeignKey('posts.id'))
	datetime = Column(DateTime)


class Like(UserMixin, SqlAlchemyBase, SerializerMixin):
	__tablename__ = "likes"
	id = Column(Integer, primary_key=True, autoincrement=True)
	author = Column(Integer, ForeignKey('users.id'))
	dislike = Column(Boolean, default=False)
	type = Column(String)
	obj_id = Column(Integer)
	datetime = Column(DateTime)
