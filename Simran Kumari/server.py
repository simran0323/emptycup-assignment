from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__
            )
CORS(app)  # Enable CORS for all routes

# Sample listings data (simulating a database)
listings_data = [
    {
        "id": 1,
        "name": "Epic Designs",
        "ratingImage": "images\rating.png",  # Path to the rating image
        "description": "Passionate team of 4 designers working out of Bangalore with an experience of 4 years.",
        "projects": 57,
        "years": 8,
        "price": "$$",
        "contact": ["+91 - 984532853", "+91 - 984532854"]
    },
    {
        "id": 2,
        "name": "Studio - D3",
        "ratingImage": "images\rating.png",  # Path to the rating image
        "description": "Passionate team of 4 designers working out of Bangalore with an experience of 4 years.",
        "projects": 43,
        "years": 6,
        "price": "$$$",
        "contact": ["+91 - 984532853", "+91 - 984532854"]
    }
]

@app.route('/listings', methods=['GET'])
def get_listings():
    return jsonify(listings_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)