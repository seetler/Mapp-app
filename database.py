# database.py
import sqlite3
import random

# Create SQLite database and table for storing locations if it doesn't exist
def init_db():
    conn = sqlite3.connect('locations.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS locations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            lat REAL,
            lng REAL
        )
    ''')

    # Insert fixed locations if they don't already exist
    cursor.execute('SELECT COUNT(*) FROM locations WHERE name = "San Francisco"')
    if cursor.fetchone()[0] == 0:
        cursor.execute('INSERT INTO locations (name, lat, lng) VALUES (?, ?, ?)', ("San Francisco", 37.7649, -122.4194))

    cursor.execute('SELECT COUNT(*) FROM locations WHERE name = "New York"')
    if cursor.fetchone()[0] == 0:
        cursor.execute('INSERT INTO locations (name, lat, lng) VALUES (?, ?, ?)', ("New York", 40.7306, -73.9352))

    conn.commit()
    conn.close()

# Insert or update random locations
def insert_random_locations():
    conn = sqlite3.connect('locations.db')
    cursor = conn.cursor()

    # Delete random locations, but keep San Francisco and New York
    cursor.execute('DELETE FROM locations WHERE name LIKE "Random%"')
    
    # Insert random locations into the table
    for i in range(1, 6):  # Random 1 to Random 5
        name = f"Random {i}"
        lat = random.random() * 3 + 37  # Random lat value near 37
        lng = random.random() * 48.48 - 122.4194  # Random lng value near -122.4194
        cursor.execute('INSERT INTO locations (name, lat, lng) VALUES (?, ?, ?)', (name, lat, lng))
    
    conn.commit()
    conn.close()

# Get all locations from the database
def get_locations():
    conn = sqlite3.connect('locations.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, lat, lng FROM locations')
    locations = cursor.fetchall()
    conn.close()
    
    # Format the data into a list of dictionaries for the frontend
    return [{"name": name, "lat": lat, "lng": lng} for name, lat, lng in locations]
