from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb+srv://Aurelioprod:U0PWxXrhk4KmFpp4@vulcaotech-pdii4.mongodb.net/Generic?retryWrites=true&w=majority"

mongo = PyMongo(app)

# @app.route('/')
# def hello():
#     return "hello"


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



# mongo = PyMongo(app)
# app.config['MONGO_URI'] = "mongodb+srv://Aurelioprod:U0PWxXrhk4KmFpp4@vulcaotech-pdii4.mongodb.net/Generic?retryWrites=true&w=majority"

# @app.route('/', methods=['POST'])
# def add_user():
#     _json = request.json
#     _name = _json['name']
#     _name2 = _json['name2']
#     _password = _json['pwd']

#     if _name and _name2 and _password and request.method == 'POST':
#         _hashed_password = generate_password_hash(_password)

#         # depois do db. devo colocar o nome do meu cluster
#         id = mongo.db.anydatas.insert(
#             {'name': _name, 'name2': _name2, 'pwd': _hashed_password})
#         resp = jsonify('Add successfully')
#         resp.status_code = 200
#         return resp

#     else:
#         return not_found()


# @app.errorhandler(404)
# def not_found(error=None):
#     message = {
#         'status': 404,
#         'message': 'Not found' + request.url
#     }
#     resp = jsonify(message)
#     resp.status_code = 404
#     return resp
