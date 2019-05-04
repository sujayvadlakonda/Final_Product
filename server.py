from flask import Flask, render_template, jsonify
from flask_cors import CORS
import Config
import web_scrape
from database import Database
from bson.json_util import dumps

app = Flask(__name__)
CORS(app)
app.secret_key = 'shushmans'

Database.initialize()
# web_scrape.web_scrape()

data = {
    'centennial': {
        'T-Shirts': [],
        'Sweatshirts': [],
        'Hats': [],
        'Men': [],
        'Women': [],
        'Youth': [],
        'Top Sellers': []
    },

    'frisco': {
        'T-Shirts': [],
        'Sweatshirts': [],
        'Hats': [],
        'Men': [],
        'Women': [],
        'Youth': [],
        'Top Sellers': []
    },

    'heritage': {
        'T-Shirts': [],
        'Sweatshirts': [],
        'Hats': [],
        'Men': [],
        'Women': [],
        'Youth': [],
        'Top Sellers': []
    },

    'independence': {
        'T-Shirts': [],
        'Sweatshirts': [],
        'Hats': [],
        'Men': [],
        'Women': [],
        'Youth': [],
        'Top Sellers': []
    },

    'lebanon-trail': {
        'T-Shirts': [],
        'Sweatshirts': [],
        'Hats': [],
        'Men': [],
        'Women': [],
        'Youth': [],
        'Top Sellers': []
    },

    'liberty': {
        'T-Shirts': [],
        'Sweatshirts': [],
        'Hats': [],
        'Men': [],
        'Women': [],
        'Youth': [],
        'Top Sellers': []
    },

    'lone-star': {
        'T-Shirts': [],
        'Sweatshirts': [],
        'Hats': [],
        'Men': [],
        'Women': [],
        'Youth': [],
        'Top Sellers': []
    },

    'memorial': {
        'T-Shirts': [],
        'Sweatshirts': [],
        'Hats': [],
        'Men': [],
        'Women': [],
        'Youth': [],
        'Top Sellers': []
    },

    'reedy': {
        'T-Shirts': [],
        'Sweatshirts': [],
        'Hats': [],
        'Men': [],
        'Women': [],
        'Youth': [],
        'Top Sellers': []
    },

    'wakeland': {
        'T-Shirts': [],
        'Sweatshirts': [],
        'Hats': [],
        'Men': [],
        'Women': [],
        'Youth': [],
        'Top Sellers': []
    },
}

for school, categories in data.items():
    for category, products in categories.items():
        cursor = Database.find(school, {'category': category})
        for product in cursor:
            products.append(product)


@app.route('/')
def index():
    return render_template('home.html', data=data)


@app.route('/test')
def test():
    return "<h5>" + web_scrape.test().__repr__() + "</h5>"


@app.route('/data')
def yoshidata():
    return str(dumps(data))


if __name__ == '__main__':
    app.run(debug=Config.DEBUG, port=5990)
