# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import ForeignKey
# from sqlalchemy import String, Integer

# app = Flask(__name__)
# db = SQLAlchemy()

# class User(db.Model):
#     __tablename__ = 'users'
    
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30), nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), unique=False, nullable=False)
    
#     planetas = db.relationship('Favorite_Planet', backref='user', lazy=True)
#     personajes = db.relationship('Favorite_Character', backref='user', lazy=True)

#     def serialize(self):
#         return {
#             "id": self.id,
#             "name": self.name,
#             "email": self.email          
#         }
    

# class Character(db.Model):
#     __tablename__ = 'characters'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(String(50), nullable=False)
#     height = db.Column(db.String(80), unique=False, nullable=False)
    
#     personajes = db.relationship('Favorite_Character', backref='character', lazy=True)

#     def serialize(self):
#         return {
#             "id": self.id,
#             "name": self.name,
#             "height": self.height
#         }    

# class Planet(db.Model):
#     __tablename__ = 'planets'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(String(50), nullable=False)
#     poblacion = db.Column(String(50), nullable=False)
       
#     planetas = db.relationship('Favorite_Planet', backref='planet', lazy=True)
       
#     def serialize(self):
#         return {
#             "id": self.id,
#             "name": self.name,
#             "poblacion": self.poblacion
#         }

# class Favorite_Planet(db.Model):
#     __tablename__ = 'favorite_planet'
#     user_id = db.Column(Integer, ForeignKey('users.id'), primary_key=True)
#     planet_id = db.Column(Integer, ForeignKey('planets.id'), primary_key=True)

#     # user = db.relationship('User', backref='planeta_favorito', lazy=True)
#     # planet = db.relationship('Planet', backref='planetas', lazy=True)

#     def serialize(self):
#         return {
#             "user_id": self.user_id,
#             "planet_id": self.planet_id
#         }

# class Favorite_Character(db.Model):
#     __tablename__ = 'favorite_character'
#     user_id = db.Column(Integer, ForeignKey('users.id'), primary_key=True)
#     character_id = db.Column(Integer, ForeignKey('characters.id'), primary_key=True)

#     # user = db.relationship('User', backref='favorite_people', lazy=True)
#     # character = db.relationship('Character', backref='personajes', lazy=True)

#     def serialize(self):
#         return {
#             "user_id": self.user_id,
#             "character_id": self.character_id
#         }
