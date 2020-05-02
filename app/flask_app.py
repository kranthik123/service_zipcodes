from flask import Flask
from flask import make_response
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def main():
    products_list = ["Rain Coat", "Rain Boots"]
    return jsonify(products_list)

@app.route('/<page_name>')
def other_page(page_name):
    response = make_response('The page named %s does not exist.' % page_name, 404)
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='4000')
