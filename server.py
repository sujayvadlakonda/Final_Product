from flask import Flask, jsonify
from flask_cors import CORS
import Config
import web_scrape

app = Flask(__name__)
CORS(app)
app.secret_key = 'shushmans'

web_scrape.web_scrape()


@app.route('/')
def index():
    return "<h5>" + web_scrape.data.__repr__() + "</h5>"


@app.route('/test')
def test():
    json = {'hello': 'world'}
    return jsonify(json)


app.run(debug=Config.DEBUG)
