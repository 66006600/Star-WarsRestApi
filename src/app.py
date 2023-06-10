"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, abort
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
from models import User, Character, Planet, Favorite_Planet, Favorite_Character


app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)
   
@app.route('/user', methods=['GET'])
def handle_hello():
    users = User.query.all()    
    result = list(map(lambda user:user.serialize(),users))
    return jsonify(result)


@app.route('/character', methods=['GET'])
def get_characters():
    characters = Character.query.all()    
    result = list(map(lambda character:character.serialize(),characters))
    return jsonify(result)

@app.route('/planets', methods=['GET'])
def get_planets():
    planets = Planet.query.all()    
    result = list(map(lambda planet:planet.serialize(),planets))
    return jsonify(result)




@app.route('/planets', methods=['POST'])
def create_planet():
    data = request.get_json()
    new_planet = Planet(name=data['name'], poblacion=data['poblacion'])
    print("jsjs")
    db.session.add(new_planet)
    db.session.commit()
  
    return jsonify({"mensaje": "Se ha agregado un nuevo planeta"}), 201


@app.route('/characters', methods=['POST'])
def create_character():
    data = request.get_json()
    new_character = Character(name=data['name'], height=data['height'])
    print("jsjs")
    db.session.add(new_character)
    db.session.commit()
  
    return jsonify({"mensaje": "Se ha agregado un nuevo personaje"}), 201

@app.route('/planets/<id>', methods=['DELETE'])
def delete_planet(id):
    print(id)
    planet = Planet.query.filter(Planet.id == id).one_or_none()
    if planet == None:
        abort(404)
    db.session.delete(planet)
    db.session.commit()
    return jsonify({'result': 'success'})
    
@app.route('/character/<id>', methods=['DELETE'])
def delete_character(id):
    print(id)
    character = Character.query.filter(Character.id == id).one_or_none()
    if character == None:
        abort(404)
    db.session.delete(character)
    db.session.commit()
    return jsonify({'result': 'success'})
    

@app.route('/user/favorite_character/<int:user_id>', methods=['POST'])
def add_favorite_character(user_id):
    user_id = User.query.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()
    character_id = data.get('character_id')
    if character_id is None:
        return jsonify({'error': 'Invalid request'}), 400

    favorite_character = Favorite_Character(user=user, character=character)
    db.session.add(favorite_character)
    db.session.commit()

    return jsonify({
        'user_id': user.id,
        'character_id': character.id
     }), 201


# @app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
# def manage_favorite_planet(planet_id):

#     user = query.get(user_id)

#     favorite_planet = Favorite_Planet(planet_id=request.json['planet'])

#     db.session.add(favorite_planet)
#     db.session.commit()
#     return jsonify(favorite_planet.serialize()), 201


# @app.route('/favorite/planet/<int:planet_id>', methods=['POST', 'DELETE'])
# def manage_favorite_planet(planet_id):
#     if request.method == 'POST':

#         if Favorite_Planet.query.filter_by(user_id=1, planet_id=planet_id).first():
#             return jsonify({'message': 'El planeta ya es un favorito'}), 409

#         favorite_planet = Favorite_Planet(user_id=1, planet_id=planet_id)
#         db.session.add(favorite_planet)
#         db.session.commit()

#         return jsonify({'message': 'Planeta agregado como favorito'}), 201

#     elif request.method == 'DELETE':
#         if planet_id not in planets_db:
#             abort(404)
#         deleted_planet = planets_db.pop(planet_id)
#         db.session.commit()
#         return jsonify({'result': 'success', 'deleted': deleted_planet})


#     #return jsonify({'message': 'Método inválido'}), 405


# @app.route('/favorite/character/<int:character_id>', methods=['POST', 'DELETE'])
# def manage_favorite_character(character_id):
#     if request.method == 'POST':

#         if Favorite_Character.query.filter_by(user_id=1, character_id=character_id).first():
#             return jsonify({'message': 'El personaje ya es tu favorito'}), 409

#         favorite_character = Favorite_Character(
#             user_id=1, character_id=character_id)
#         db.session.add(favorite_character)
#         db.session.commit()
#         return jsonify({'message': 'Personaje agregado como favorito'}), 201

#     elif request.method == 'DELETE':

#         if favorite_character not in favorite_character_db:
#             abort(404)
#         deleted_favorite_character = favorite_character_db.pop(favorite_character)
#         db.session.commit()
#         print(deleted_favorite_character)
#         return jsonify({'result': 'success', 'deleted': deleted_favorite_Character})


# @app.route('/planets', methods=['GET', 'PUT', 'POST'])
# def get_planets():
#     if request.method == 'GET':
#         planets = Planet.query.all()
#         return jsonify([planet.serialize() for planet in planets]), 200

#     elif request.method == 'PUT':
#         planet_id = request.json.get('planet_id')
#         planet_name = request.json.get('planet_name')
#         planet = Planet.query.get(planet_id)

#         if not planet:
#             return jsonify({'message': 'El planeta no existe'}), 404

#         planet.name = planet_name
#         db.session.commit()
#         return jsonify(planet.serialize()), 200

#     elif request.method == 'POST':
#         planet_name = request.json.get('planet_name')

#         new_planet = Planet(name=planet_name)
#         db.session.add(new_planet)
#         db.session.commit()
#         return jsonify({'message': 'Planeta agregado correctamente', 'planet': new_planet.serialize()}), 201

#     else:
#         return jsonify({'message': 'Invalid method'}), 405


# @app.route('/characters', methods=['GET', 'PUT', 'POST'])
# def get_characters():

#         if request.method == 'GET':
#             characters = Character.query.all()
#             return jsonify(Character.serialize()), 200

#         elif request.method == 'PUT':
#             character_id = request.json.get('character_id')
#             character_name = request.json.get('character_name')
#             character = Character.query.get(character_id)

#             if not character:
#                 return jsonify({'message': 'El personaje no existe'}), 404

#             character.name = character_name
#             db.session.commit()
#             return jsonify(character.serialize()), 200

#         elif request.method == 'POST':
#             character_name = request.json.get('character_name')
#             new_character = Character(name=character_name)

#             db.session.add(new_character)
#             db.session.commit()
#             return jsonify({'message': 'Personaje agregado correctamente'}), 201

#         else:
#             return jsonify({'message': 'Invalid method'}), 405

# @app.route('/character/<string:character_id>', methods=['DELETE'])
# def delete_character(character_id):
#     if character_id not in characters_db:
#         abort(404)
#     deleted_character = characters_db.pop(character_id)
#     print(deleted_character)
#     db.session.commit()
#     return jsonify({'result': 'success', 'deleted': deleted_character})


# @app.route('/planet/<string:planet_id>', methods=['DELETE'])
# def delete_planet(planet_id):
#     if planet_id not in planets_db:
#         abort(404)
#     deleted_planet = planets_db.pop(planet_id)
#     print(deleted_planet)
#     db.session.commit()
#     return jsonify({'result': 'success', 'deleted': deleted_planet})

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
