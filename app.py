import json

from pprint import pprint

from flask import Flask, jsonify, render_template, request, url_for
from flask_cors import CORS



app = Flask(__name__)
CORS(app, support_credentials=True)

lobbies = {
    'lobby1': {
        'host': '',
        'players': [],
        'started': False,
    }
}

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/joinLobby", methods=['POST'])
def joinLobby():
    data = json.loads(str(request.data, 'UTF-8'))
    lobbies[data['lobbyId']]['players'].append(data['phoneNumber'])

    pprint(lobbies)

    return jsonify({'success': 'you have joined the lobby'})

if __name__ == '__main__':
    app.run(debug=True)
