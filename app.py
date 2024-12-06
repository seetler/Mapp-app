# app.py
from flask import Flask, render_template, jsonify, request, redirect, url_for
from datetime import datetime
import sqlite3
from database import init_db, insert_random_locations, get_locations

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def data():
    # Insert random locations into the database whenever the page is visited
    insert_random_locations()
    
    # Fetch data from the SQLite database and return as JSON
    locations = get_locations()
    return jsonify(locations)


if __name__ == '__main__':
    # Initialize the database before the app runs
    init_db()

    # Run the Flask app on all available IP addresses
    app.run(host='0.0.0.0', port=5000, debug=True)
