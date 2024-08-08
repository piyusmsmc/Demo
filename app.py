from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/concatenate', methods=['GET'])
def concatenate():
    string1 = request.args.get('string1', '')
    string2 = request.args.get('string2', '')
    string3 = request.args.get('string3', '')
    
    concatenated_string = string1 + string2 + string3
    return jsonify({"concatenated_string": concatenated_string})

if __name__ == '__main__':
    app.run(debug=True)
