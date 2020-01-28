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
    
    return render_template('index.html', word_counter=mongo.db.words.find().count(), last_words=mongo.db.words.find().sort([{'date',-1}]).limit(3))
    



@app.route('/get_word', methods=['POST'])
def get_word():
    word = request.form.get('word_definition')
    return render_template("word_definition.html", words=mongo.db.words.find({'name': {'$regex': word, '$options': 'i'}}))

@app.route('/add_word')
def add_word():
    return render_template("insert_word.html")

@app.route('/insert_word', methods=['POST'])
def insert_word():
    words_dict = request.form.to_dict()
    word = mongo.db.words
    word.insert_one(words_dict)
    return redirect(url_for('conrats_insert'))

@app.route('/conrats_insert')
def conrats_insert():
    return render_template("congrats_insert.html")
    
@app.route('/delete_word/<word_id>')
def delete_word(word_id):
    mongo.db.words.remove({'_id': ObjectId(word_id)})
    return redirect(url_for('congrats_remove'))
    
@app.route('/congrats_remove')
def congrats_remove():
    return render_template("congrats_remove.html")



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            