# start with a basic flask application setup
from flask import Flask, render_template
from dotenv import load_dotenv
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')

# Registering blueprints for different modules
from routes.auth import auth_bp
from routes.spotify import spotify_bp
#from routes.other_routes import other_bp

@app.route('/')
def index():
    '''
    Renders the index.html template when the root URL is accessed.

    Returns:
        rendered_template: HTML content for the index page.
    '''
    return render_template('index.html')

@app.route('/playlist')
def playlist():
    '''
    Renders the playlist.html template when the '/playlist' URL is accessed.

    Returns:
        rendered_template: HTML content for the playlist page.
    '''
    return render_template('playlist.html')

app.register_blueprint(auth_bp)
app.register_blueprint(spotify_bp)
#app.register_blueprint(other_bp)

if __name__ == '__main__':
    app.run(debug=True)