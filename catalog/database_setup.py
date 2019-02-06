#!/usr/bin/env python3

import sys
import os
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):

    # User Table

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

    @property
    def serializable(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email}


class GameType(Base):

    # Game Type here

    __tablename__ = 'gametype'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serializable(self):
        return {
            'name': self.name,
            'id': self.id}


class PCGames(Base):

    # PCGames Table

    __tablename__ = 'pcgames'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    image = Column(String)
    release_date = Column(String, nullable=False)
    company = Column(String, nullable=False)
    game_type_id = Column(Integer, ForeignKey('gametype.id'))
    game_type = relationship(GameType)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serializable(self):
        return {
            'name': self.name,
            'id': self.id,
            'description': self.description,
            'release_date': self.release_date,
            'company': self.company,
            'game_type': self.game_type.name}

engine = create_engine('sqlite:///pcgames.db')

Base.metadata.create_all(engine)
