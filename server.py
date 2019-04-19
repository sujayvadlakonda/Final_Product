from flask import Flask, render_template
from flask_cors import CORS
import Config
import web_scrape
from database import Database

app = Flask(__name__)
CORS(app)
app.secret_key = 'shushmans'

Database.initialize()
# web_scrape.web_scrape()
data = Database.find('frisco', {'category': 'Top Sellers'})


@app.route('/')
def index():
    return render_template('home.html', data=data)


@app.route('/test')
def test():
    return "<h5>" + web_scrape.test().__repr__() + "</h5>"

@app.route('/data')
def data():
    # data = Database...
    # return jsonify(data)

if __name__ == '__main__':
    app.run(debug=Config.DEBUG, port=5990)
