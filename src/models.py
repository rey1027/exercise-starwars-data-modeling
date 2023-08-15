import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class FavoritesPerson(Base):
    __tablename__ = 'favoritesperson'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    person_id = Column(Integer, ForeignKey('person.id'))
    rating = Column(Integer, nullable = True) 

class FavoritesPlanet(Base):
    __tablename__ = 'favoritesplanet'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))

class FavoritesVehicle(Base):
    __tablename__ = 'favoritesvehicle'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))  

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    birth_year = Column(String(40), nullable = False)
    eyes_color = Column(String(20), nullable = True)
    films = Column(String(100), nullable = True)
    gender = Column(String(20), nullable=False)
    height = Column(Integer,nullable = True)
    homeworld = Column(String(100), nullable = True)
    mass= Column(Integer,nullable = True)
    name = Column(String(100), nullable=False)
    skin_color = Column(String(50), nullable=False) 
    created = Column(String(100), nullable=False)
    edited = Column(String(100), nullable=False)  
    species = Column(String(100), nullable = True)
    starships = Column(String(100), nullable = True)
    url = Column(String(100), nullable = True)
    vehicule = Column(String(100), nullable = True)
    favorites_person = relationship(FavoritesPerson, backref='person', lazy=True) #backref es una autoreferencia

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    climate = Column(String(40), nullable = False)
    created = Column(String(100), nullable=True)
    diameter = Column(Integer,nullable = True)
    edited = Column(String(50), nullable = True)
    films = Column(String(100), nullable = True)
    gravity = Column(String(20), nullable=False)
    name = Column(String(50), nullable=False)
    orbital_period = Column(String(50), nullable=True)
    population = Column(Integer,nullable = True) 
    residents = Column(String(70), nullable=False)  
    rotation_period = Column(Integer, nullable = True)
    surface_water = Column(Integer, nullable = True)
    terrain = Column(String(60), nullable = False)
    url = Column(String(100), nullable = True)
    favorites_planet = relationship(FavoritesPlanet, backref='person', lazy=True) #backref es una autoreferencia

class Vehicle(Base):
    __tablename__ = 'vehicle'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    cargo_capacity = Column(Integer, nullable = False)
    consumables = Column(String(20), nullable = True)
    cost_in_credits = Column(Integer, nullable = True)
    created = Column(String(30), nullable=False)
    crew = Column(Integer,nullable = True)
    edited = Column(String(50), nullable = True)
    length=Column(Integer,nullable = True)
    manufacturer = Column(String(100), nullable=False)
    max_atmosphering_speed = Column(Integer, nullable=False) 
    model = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)  
    passengers = Column(Integer, nullable = True)
    pilots = Column(String(50), nullable = True)
    films = Column(String(100), nullable = True)
    url = Column(String(100), nullable = True)
    vehicle_class= Column(String(25), nullable = True)
    #Cambiar 
    favorites_vehicle = relationship(FavoritesVehicle, backref='vehicle', lazy=True) #backref es una autoreferencia


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False)
    favorites_person = relationship(FavoritesPerson, backref='user', lazy=True)




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
