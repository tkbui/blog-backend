from flask import Flask, jsonify
from flask_cors import CORS

# create Flask app instance
app = Flask(__name__)
CORS(app)

# example route
@app.route('/api/home', methods=["GET"])
def return_home():
    return jsonify({
      'message': 'Hello World!'
    })

# way to run the app
if __name__ == '__main__':
  # debug=True lets app know we're in dev mode; remove for prod
  app.run(debug=True, port=8080)