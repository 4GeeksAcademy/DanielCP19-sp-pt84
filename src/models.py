import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(25), nullable=False, unique=True)
    password = Column(String(25), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    first_name = Column(String(25))
    last_name = Column(String(25))
    date_subscription = Column(Date)
    favorite_planet = relationship('FavoritePlanet', back_populates='user')
# Fav*_planets > user = relationship(User, back_populates='favorite_planet')
    favorite_character = relationship('FavoriteCharacter', back_populates='user')
# Fav*_characters > user = relationship(User, back_populates='favorite_character')


class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False, unique=True)
    diameter = Column(Integer)
    climate = Column(String(25))
    population = Column(Integer)
    terrain = Column(String(25))
    url = Column(String(255))
    habitant = relationship('Character', back_populates='planet')
# Characters > planet = relationship(Planet, back_populate='habitant')
    favorite_planet_of = relationship('FavoritePlanet', back_populates='planet')
#Fav*_plantes > planet = relationship(Planet, back_populates='favorite_planet_of')


class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False, unique=True)
    gender = Column(Enum('male', 'female', name='gender_enum'))
    height = Column(Integer)
    mass = Column(Integer)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship(Planet, back_populates='habitant')
    url = Column(String(255))
    favorite_character_of = relationship('FavoriteCharacter', back_populates='character')
#Fav*_characters > character = relationship(Character, back_populates='favorite_character_of')


class FavoritePlanet(Base):
    __tablename__ = 'favorite_planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User, back_populates='favorite_planet')
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship(Planet, back_populates='favorite_planet_of')


class FavoriteCharacter(Base):
    __tablename__ = 'favorite_characters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User, back_populates='favorite_character')
    character_id = Column(Integer, ForeignKey('characters.id'))
    character = relationship(Character, back_populates='favorite_character_of')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
