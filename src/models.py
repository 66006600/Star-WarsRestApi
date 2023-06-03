from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer


app = Flask(__name__)
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    personajes = db.relationship('Favorite_Character', backref='usuario')
    planetas = db.relationship('Favorite_Planet', backref='usuario')
    

class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    height = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorits = db.relationship('FavoriteCharacter', backref='personajes')

class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(String(50), nullable=False)
    poblacion = db.Column(String(50), nullable=False)   
    favoritos = db.relationship('FavoritePlanet', backref='planetas')

class Favorite_Planet(db.Model):
    __tablename__ = 'favorite_planet'
    user_id = db.Column(Integer, ForeignKey('user.id'), primary_key = True)
    planet_id = db.Column(Integer, ForeignKey('planet.id'), primary_key = True)

    users = db.relationship(User, back_populates="favorite_planet")

   
class Favorite_Character(db.Model):
    __tablename__ = 'favorite_character'   
    user_id = db.Column(Integer, ForeignKey('user.id'), primary_key = True)
    character_id = db.Column(Integer, ForeignKey('character.id'), primary_key = True)

    users = db.relationship(User, back_populates="favorite_character")


    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
