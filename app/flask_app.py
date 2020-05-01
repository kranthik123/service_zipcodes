from flask import Flask
from flask import make_response
import json
from flask import jsonify
from flask import request
import re

app = Flask(__name__)

@app.route('/')
def main():
    zipcode_list = []
    with open('zipcodes.json') as json_file:
        contents = json.load(json_file)
    for l in contents['data']:
        zipcode_list.append(l['zipcode'])
    return jsonify(zipcode_list)


@app.route('/zipcode')
def zipcode():
    zipc = request.args.get('zipcode')
    pattern = "^[0-9]{5}(?:-[0-9]{4})?$"
    if re.match(pattern, zipc):
        response = make_response('Valid zipcode entered: %s.' % zipc)
        return response
    else:
        response = make_response('Invalid zipcode provided: %s.' % zipc)
        return response

@app.route('/<page_name>')
def other_page(page_name):
    response = make_response('The page named %s does not exist.' % page_name, 404)
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='4000')
