from routes import register_blueprints
from flask import Flask

app = Flask(__name__)

# Register blueprints
register_blueprints(app)

if __name__ == '__main__':
    app.run()