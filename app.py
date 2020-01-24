import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'dictionary'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')


mongo = PyMongo(app)


@app.route('/')
def index():
    
    return render_template('index.html',word_counter=mongo.db.words.find().count(), last_words=mongo.db.words.find().sort([{'date' ,1}]).limit(3))
    



@app.route('/get_word', methods=['POST'])
def get_word():
    word = request.form.get('word_definition')
    return render_template("word_definition.html", words=mongo.db.words.find({'name': {'$regex': word, '$options': 'i'}}))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            