from flask import Flask
from flask import make_response
import json
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def main():
    zipcode_list = []
    with open('zipcodes.json') as json_file:
        contents = json.load(json_file)
    for l in contents['data']:
        zipcode_list.append(l['zipcode'])
    return jsonify(zipcode_list)

@app.route('/<page_name>')
def other_page(page_name):
    response = make_response('The page named %s does not exist.' % page_name, 404)
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='4000')
