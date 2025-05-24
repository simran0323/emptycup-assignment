from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = sqlite3.connect('listings.db')
    conn.row_factory = sqlite3.Row  # Allows us to return rows as dictionaries
    return conn

@app.route('/api/listings', methods=['GET'])
def get_listings():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Fetch all listings
    cursor.execute('SELECT * FROM listings')
    listings = cursor.fetchall()

    # Fetch contacts for each listing and format the response
    result = []
    for listing in listings:
        cursor.execute('SELECT phone FROM contacts WHERE listing_id = ?', (listing['id'],))
        contacts = [row['phone'] for row in cursor.fetchall()]
        
        listing_dict = {
            'id': listing['id'],
            'name': listing['name'],
            'description': listing['description'],
            'projects': listing['projects'],
            'years': listing['years'],
            'price': listing['price'],
            'contact': contacts
        }
        result.append(listing_dict)

    conn.close()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)