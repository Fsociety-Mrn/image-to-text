# app.py
from flask import Flask
from views import pages
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
 

app.register_blueprint(pages)


if __name__ == '__main__':
    app.run(
        # host='192.168.100.134',
        host='0.0.0.0',
        debug=True,
        port=1000) 