# start with a basic flask application setup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# other routes and functionality will go here

if __name__ == '__main__':
    app.run(debug=True)