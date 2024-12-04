from flask import Flask
import sqlite3

app = Flask(__name__, static_folder='../static', static_url_path='/static')

app.config['SECRET_KEY'] = 'supersecretkey'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

from app import routes