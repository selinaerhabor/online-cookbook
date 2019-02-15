import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"]  = 'online-cookbook'
app.config["MONGO_URI"] = 'mongodb://admin:u537a6m1n@ds213665.mlab.com:13665/online-cookbook'

mongo = PyMongo(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template("cuisines.html",
    cuisines=mongo.db.cuisines.find())
    
    
@app.route('/load_listofrecipes')
def load_listofrecipes():
    return render_template("listofrecipes.html",
    recipes=mongo.db.recipes.find())

@app.route('/load_recipe')
def load_recipe():
    return render_template("recipe.html",
    recipes=mongo.db.recipes.find())
    
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)