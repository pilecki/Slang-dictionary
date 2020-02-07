import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
from datetime import datetime
from datetime import date

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'dictionary'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')


mongo = PyMongo(app)


@app.route('/')
def index():
    
    return render_template('index.html', word_counter=mongo.db.words.find().count(), last_words=mongo.db.words.find().sort([{'current_datetime', -1}]).limit(3))
    
    


@app.route('/get_word', methods=['POST'])
def get_word():
    word = request.form.get('word_definition')
    return render_template("word_definition.html", words=mongo.db.words.find({'name': {'$regex': word, '$options': 'i'}}))



@app.route('/add_word')
def add_word():
    
    return render_template("insert_word.html",  today = date.today(), current_datetime = datetime.now() )


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
    


@app.route('/edit_word/<word_id>')
def edit_word(word_id):
    edited_categories = mongo.db.words.find({},{ "_id": 0, "category": 1}) 
    edited_word = mongo.db.words.find_one({"_id": ObjectId(word_id)})
    return render_template('edit_word.html', word=edited_word, edited_category=edited_categories, today = date.today(), current_datetime = datetime.now())

@app.route('/update_word/<word_id>', methods=['POST'])
def update_word(word_id):
    words = mongo.db.words
    words.update({'_id': ObjectId(word_id)},
            {
                'name': request.form.get('name'),
                'meaning': request.form.get('meaning'),
                'example': request.form.get('example'),
                'category': request.form.get('category'),
                'date': request.form.get('date'),
                'author': request.form.get('author'),
                'current_datetime': request.form.get('current_datetime'),

            })
    return redirect(url_for('index'))



    
@app.route('/categories/<cat>')
def categories(cat):
    music_category = mongo.db.words.find({'category': (cat)})
    school_category = mongo.db.words.find({'category': (cat)})
    house_category = mongo.db.words.find({'category': (cat)})
    work_category = mongo.db.words.find({'category': (cat)})
    food_category = mongo.db.words.find({'category': (cat)})
    internet_category = mongo.db.words.find({'category': (cat)})
    common_category = mongo.db.words.find({'category': (cat)})
    
    if cat == cat:
        return render_template("category.html", category=music_category)
    elif cat == cat:
        return render_template("category.html", category=house_category)
    elif cat == cat:
        return render_template("category.html", category=school_category)
    elif cat == cat:
        return render_template("category.html", category=work_category)
    elif cat == cat:
        return render_template("category.html", category=food_category)
    elif cat == cat:
        return render_template("category.html", category=internet_category)
    elif cat == cat:
        return render_template("category.html", category=common_category)
   
   
        
@app.route('/letters/<let>')
def letters(let):
    a = mongo.db.words.find({ 'name': { "$regex": "^a", '$options': 'i'} })
    b = mongo.db.words.find({ "name": { "$regex": "^b", '$options': 'i'} })
    c = mongo.db.words.find({ "name": { "$regex": "^c", '$options': 'i' } })
    d = mongo.db.words.find({ "name": { "$regex": "^d", '$options': 'i' } })
    e = mongo.db.words.find({ "name": { "$regex": "^e", '$options': 'i' } })
    f = mongo.db.words.find({ "name": { "$regex": "^f", '$options': 'i' } })
    g = mongo.db.words.find({ "name": { "$regex": "^g", '$options': 'i' } })
    h = mongo.db.words.find({ "name": { "$regex": "^h", '$options': 'i' } })
    i = mongo.db.words.find({ "name": { "$regex": "^i", '$options': 'i' } })
    j = mongo.db.words.find({ "name": { "$regex": "^j", '$options': 'i' } })
    k = mongo.db.words.find({ "name": { "$regex": "^k", '$options': 'i' } })
    l = mongo.db.words.find({ "name": { "$regex": "^l", '$options': 'i' } })
    m = mongo.db.words.find({ "name": { "$regex": "^m", '$options': 'i' } })
    n = mongo.db.words.find({ "name": { "$regex": "^n", '$options': 'i' } })
    o = mongo.db.words.find({ "name": { "$regex": "^o", '$options': 'i' } })
    p = mongo.db.words.find({ "name": { "$regex": "^p", '$options': 'i' } })
    q = mongo.db.words.find({ "name": { "$regex": "^q", '$options': 'i' } })
    r = mongo.db.words.find({ "name": { "$regex": "^r", '$options': 'i' } })
    s = mongo.db.words.find({ "name": { "$regex": "^s", '$options': 'i' } })
    t = mongo.db.words.find({ "name": { "$regex": "^t", '$options': 'i' } })
    u = mongo.db.words.find({ "name": { "$regex": "^u", '$options': 'i' } })
    v = mongo.db.words.find({ "name": { "$regex": "^v", '$options': 'i' } })
    w = mongo.db.words.find({ "name": { "$regex": "^w", '$options': 'i' } })
    x = mongo.db.words.find({ "name": { "$regex": "^x", '$options': 'i' } })
    y = mongo.db.words.find({ "name": { "$regex": "^y", '$options': 'i' } })
    z = mongo.db.words.find({ "name": { "$regex": "^z", '$options': 'i' } })
   
    if let == 'a':
        return render_template("letters.html", letter = a)
    elif let == 'b':
        return render_template("letters.html", letter = b)
    elif let == 'c':
        return render_template("letters.html", letter = c)
    elif let == 'd':
        return render_template("letters.html", letter = d)
    elif let == 'e':
        return render_template("letters.html", letter = e)
    elif let == 'f':
        return render_template("letters.html", letter = f)
    elif let == 'g':
        return render_template("letters.html", letter = g)
    elif let == 'h':
        return render_template("letters.html", letter = h)
    elif let == 'i':
        return render_template("letters.html", letter = i)
    elif let == 'j':
        return render_template("letters.html", letter = j)
    elif let == 'k':
        return render_template("letters.html", letter = k)
    elif let == 'l':
        return render_template("letters.html", letter = l)
    elif let == 'm':
        return render_template("letters.html", letter = m)
    elif let == 'n':
        return render_template("letters.html", letter = n)
    elif let == 'o':
        return render_template("letters.html", letter = o)
    elif let == 'p':
        return render_template("letters.html", letter = p)
    elif let == 'q':
        return render_template("letters.html", letter = q)
    elif let == 'r':
        return render_template("letters.html", letter = r)
    elif let == 's':
        return render_template("letters.html", letter = s)
    elif let == 't':
        return render_template("letters.html", letter = t)
    elif let == 'u':
        return render_template("letters.html", letter = u)
    elif let == 'v':
        return render_template("letters.html", letter = v)
    elif let == 'w':
        return render_template("letters.html", letter = w)
    elif let == 'x':
        return render_template("letters.html", letter = x)
    elif let == 'y':
        return render_template("letters.html", letter = y)
    elif let == 'z':
        return render_template("letters.html", letter = z)

    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            