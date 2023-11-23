# start with a basic flask application setup
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_playlist', methods=['POST'])
def generate_playlist():
    artists = request.form.get('artists')
    songs = request.form.get('songs')
    genres = request.form.get('genres')


if __name__ == '__main__':
    app.run(debug=True)