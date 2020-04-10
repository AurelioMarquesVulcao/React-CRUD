from flask import Flask, request, jsonify, Response
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb+srv://Aurelioprod:U0PWxXrhk4KmFpp4@vulcaotech-pdii4.mongodb.net/Generic?retryWrites=true&w=majority"

mongo = PyMongo(app)

# @app.route('/')
# def hello():
#     return "hello"

# metodo de envio de dados.
@app.route('/', methods=['POST'])
def create_user():
    # print(request.json)
    name = request.json['name']
    name2 = request.json['name2']
    password = request.json['password']

    if name and name2 and password:
        hashed_password = generate_password_hash(password)
        # db.anydatas - anygatas é a minha base de dados
        id = mongo.db.anydatas.insert(
            {'name': name, 'name2': name2, 'password': hashed_password}
        )
        response = {
            'id': str(id),
            'name': name,
            'name2': name2,
            'password': hashed_password

        }
        return response
    else:
        return not_found()

    return {"message": "recebido"}


# metodo de recebimento de dados
@app.route('/', methods=['GET'])
def get_users():
    # a variavél que armazena pode ser qualquer nome que se encaixe na sua aplicação
    any_data = mongo.db.anydatas.find()
    # json util torna a resposta em algo util
    response = json_util.dumps(any_data)
    # Response do flask melhora a Resposta
    return Response(response, mimetype='application/json')

# assim funciona normalmente
@app.route('/<id>', methods=['GET'])
def get_user(id):
    any_data = mongo.db.anydatas.find_one({'_id': ObjectId(id)})
    response = json_util.dumps(any_data)
    return Response(response, mimetype='application/json')


@app.route('/<id>', methods=['DELETE'])
def delete_user(id):
    mongo.db.anydatas.delete_one({'_id': ObjectId(id)})
    response = jsonify({"message": "User " + id + " was Deleted successfully"})
    return response


@app.route('/<id>', methods=['PUT'])
def update_user(id):
    name = request.json['name']
    name2 = request.json['name2']
    password = request.json['password']

    if name and name2 and password:
        hashed_password = generate_password_hash(password)
        # db.anydatas - anygatas é a minha base de dados
        mongo.db.anydatas.update_one(
            {'_id': ObjectId(id)},
            {'$set': {
                'name': name,
                'name2': name2,
                'password': hashed_password
            }})
        response = jsonify({"message": "User " + id + " was Update successfully"})
        return response


# para erros usuarios não encontrados ou problemas na base de dados
@app.errorhandler(404)
def not_found(error=None):
    response = jsonify({
        'message': 'Not Found: ' + request.url,
        'status': 404
    })
    response.status_code = 404
    return response


if __name__ == "__main__":
    # para produção desativar debug=True
    app.run(debug=True)
