# start with a basic flask application setup
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Registering blueprints for different modules
from routes.auth import auth_bp
from routes.spotify import spotify_bp

# rendering the html
@app.route('/')
def index():
    return render_template('index.html')

app.register_blueprint(auth_bp)
app.register_blueprint(spotify_bp)

if __name__ == '__main__':
    app.run(debug=True)