from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, Table, ForeignKey
from database import base


users_to_goals = Table(
    'users_to_goals',
    base.metadata,
    Column('user_id', ForeignKey('users.id')),
    Column('goals_id', ForeignKey('goals.id')),
)


class User(base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    language_lvl = Column(Float, index=True)
    goals = relationship("Goal", secondary=users_to_goals, back_populates="users")


class Goal(base):
    __tablename__ = 'goals'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    users = relationship("User", secondary=users_to_goals, back_populates="goals")


class Topic(base):
    __tablename__ = 'topics'

    name = Column(String, index=True, primary_key=True)


class Language(base):
    __tablename__ = 'language_lvl'

    language_lvl = Column(Float, index=True, primary_key=True)
