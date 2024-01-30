from flask import Flask, jsonify
from flask_cors import CORS
import json

# https://www.geeksforgeeks.org/read-json-file-using-python/
# https://www.geeksforgeeks.org/with-statement-in-python/
with open('./utils/db/games.json') as games_data:
  games = json.load(games_data)

with open('./utils/db/songs.json') as songs_data:
  songs = json.load(songs_data)

# create Flask app instance
app = Flask(__name__)
CORS(app)

# example route
@app.route('/api/home', methods=['GET'])
def return_home():
    return jsonify({
      'message': 'Hello World!'
    })

# /api/games
@app.route('/api/games', methods=['GET'])
def get_games():
    """
    Get the games and their data from games.json.

    @returns: Games <object>
    """
    return games

# /api/songs
@app.route('/api/songs', methods=['GET'])
def get_songs():
    """
    Get the songs and their data from songs.json.
    
    @returns: Games <object>
    """
    return songs

# way to run the app
if __name__ == '__main__':
  # debug=True lets app know we're in dev mode; remove for prod
  app.run(debug=True, port=8080)