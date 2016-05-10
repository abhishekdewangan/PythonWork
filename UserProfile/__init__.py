from flask import Flask
from users import test_flask
from admin import gcm
from flask_pushjack import FlaskGCM
import users
app = Flask(__name__)

config = {
    'GCM_API_KEY': 'AIzaSyD39ZdRc8tzIQJn2hK2n7V3juPnH86jmAY'
}
app.config.update(config)
client = FlaskGCM()
client.init_app(app)

@app.route('/')
def main():
    return "main route"

app.register_blueprint(test_flask.test_bp)
app.register_blueprint(users.blueprint1)
app.register_blueprint(gcm.gcm_bp)


if __name__ == '__main__':
    app.run(host='172.27.46.216')

