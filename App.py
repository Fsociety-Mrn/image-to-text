# app.py
from flask import Flask
from views import pages, api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
 

app.register_blueprint(pages)
app.register_blueprint(api)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,threaded=True) 