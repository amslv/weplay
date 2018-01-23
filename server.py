from flask import Flask, render_template, url_for, redirect, session, request
from flask.ext.pymongo import PyMongo
import bcrypt

app = Flask(__name__, static_url_path='')

"""
Configurações para conexão com MongoDB
"""
app.config['MONGODB_DBNAME'] = 'weplay'
app.config['MONGODB_URI'] = 'mongodb://admin:admin@weplay-shard-00-00-92uvs.mongodb.net:27017,weplay-shard-00-01-92uvs.mongodb.net:27017,weplay-shard-00-02-92uvs.mongodb.net:27017/test?ssl=true&replicaSet=weplay-shard-0&authSource=admin'

mongo = PyMongo(app)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongodb.db.users
        existing_user = users.find_one({'name' : request.form['username']})
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.genSalt())
            users.insert({ 'name': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            redirect(url_for(index))
        return 'Este nome de usuário já existe!'
    return app.send_static_file('/components/registration/index.view.html')

if __name__ == '__main':
    app.secret_key = 'S3CR3T!'
    app.run(debug=True)
