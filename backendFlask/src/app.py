from flask import Flask, request, jsonify, Response
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util
from bson.objectid import ObjectId
from flask_cors import CORS

app = Flask(__name__)
# tem que pesquisar qual é o metodo correto de inserir o CORS
cors = CORS(app)
# tem que pesquisar qual é o metodo correto de inserir o CORS
# CORS(app)

app.config['MONGO_URI'] = "mongodb+srv://Aurelioprod:U0PWxXrhk4KmFpp4@vulcaotech-pdii4.mongodb.net/Generic?retryWrites=true&w=majority"

mongo = PyMongo(app)

# @app.route('/')
# def hello():
#     return "hello"

# metodo de envio de dados.
@app.route('/products', methods=['POST'])
def create_user():
    # print(request.json)
    description = request.json['description']
    price = request.json['price']
    quantity = request.json['quantity']
    # password = request.json['password']

    if description and price and quantity:
        # hashed_password = generate_password_hash(password)
        # db.anydatas - anygatas é a minha base de dados
        id = mongo.db.anydatas.insert(
            {'description': description, 'price': price, 'quantity': quantity}
        )
        response = {
            'id': str(id),
            'description': description,
            'price': price,
            'quantity': quantity

        }
        return response
    else:
        return not_found()

    return {"message": "recebido"}


# metodo de recebimento de dados
@app.route('/products', methods=['GET'])
def get_users():
    # a variavél que armazena pode ser qualquer nome que se encaixe na sua aplicação
    any_data = mongo.db.anydatas.find()
    # json util torna a resposta em algo util
    response = json_util.dumps(any_data)
    # Response do flask melhora a Resposta
    return Response(response, mimetype='application/json')

# assim funciona normalmente
@app.route('/products/<id>', methods=['GET'])
def get_user(id):
    any_data = mongo.db.anydatas.find_one({'_id': ObjectId(id)})
    response = json_util.dumps(any_data)
    return Response(response, mimetype='application/json')


@app.route('/products/<id>', methods=['DELETE'])
def delete_user(id):
    mongo.db.anydatas.delete_one({'_id': ObjectId(id)})
    response = jsonify({"message": "User " + id + " was Deleted successfully"})
    return response


@app.route('/products/<id>', methods=['PUT'])
def update_user(id):
    description = request.json['description']
    price = request.json['price']
    quantity = request.json['quantity']

    if description and price and quantity:
        # hashed_password = generate_password_hash(password)
        # db.anydatas - anygatas é a minha base de dados
        mongo.db.anydatas.update_one(
            {'_id': ObjectId(id)},
            {'$set': {
                'description': description,
                'price': price,
                'quantity': quantity
            }})
        response = jsonify(
            {"message": "User " + id + " was Update successfully"})
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
    app.run(host='0.0.0.0', debug=True)
