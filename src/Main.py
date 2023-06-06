# from flask import Flask, jsonify, request
# from flask_sqlalchemy import SQLAlchemy
# from models import User, Character, Planet, Favorite_Planet, Favorite_Character


# app = Flask(__name__)
# db = SQLAlchemy(app)


# @app.route('/User', methods=['GET'])
# def get_user():
#     users = User.query.all()
#     return jsonify([user.serialize() for user in users]), 200

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
#         print(deleted_planet)
        
#         return jsonify({'result': 'success', 'deleted': deleted_planet})


#         if favorite_planet:
#             db.session.delete(favorite_planet)
#             db.session.commit()
#             return jsonify({'message': 'Planeta eliminado de favoritos'}), 200
#         else:
#             return jsonify({'message': 'El planeta no es un favorito'}), 404

#     return jsonify({'message': 'Método inválido'}), 405


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

#          if favorite_character not in favorite_character_db:
#          abort(404)
#      deleted_favorite_character = favorite_character_db.pop(favorite_character)
#      print(deleted_favorite_character)
#      return jsonify({'result': 'success', 'deleted': deleted_favorite_Character})


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
#      if character_id not in characters_db:
#          abort(404)
#      deleted_character = characters_db.pop(character_id)
#      print(deleted_character)
#      return jsonify({'result': 'success', 'deleted': deleted_character})


# @app.route('/planet/<string:planet_id>', methods=['DELETE'])
# def delete_planet(planet_id):
#      if planet_id not in planets_db:
#          abort(404)
#      deleted_planet = planets_db.pop(planet_id)
#      print(deleted_planet)
#      return jsonify({'result': 'success', 'deleted': deleted_planet})




        
        