import os
from flask import Flask, g
from peewee import SqliteDatabase

app = Flask(__name__)

# config
app.config.update(dict(
    SECRET_KEY='my_session',
    TYTUL='Expenses',
    DATABASE=os.path.join(app.root_path, 'test.db'),
))

print("my_path " + app.root_path)

# db instance
base = SqliteDatabase(app.config['DATABASE'])


@app.before_request
def before_request():
    g.db = base
    g.db.connection()


@app.after_request
def after_request(response):
    g.db.close()
    return response
