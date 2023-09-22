import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


Builds = [
    {
        "id": 1,
        "name": "SST Champion", 
        "budget": "HighEnd", 
        "pastebin": "pastebin.URL", 
        "description": "Fast and Tanky"
    },
    {   "id": 2, 
        "name": "RF Inquisitor", 
        "budget": "League-Starter", 
        "pastebin": "pastebin.URl", 
        "description": "Tanky"
    }
]

@app.route('/', methods=['GET'])
def home():
    return '''<h1>PoE Builds API</h1>
                <p>A flask api implementation for build info.</p>'''

@app.route('/builds/all', methods=['GET'])
def builds_all():
    return jsonify(Builds)

@app.route('/builds', methods=['GET'])
def builds_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an ID."
    results = []
    for build in Builds:
        if build['id'] == id:
            results.append(build)
    return jsonify(results)

@app.route('/builds', methods=['POST'])
def builds_insert():
    build = request.get_json()
    Builds.append(build)
    return "Success: build added"

@app.route('/builds/<id>', methods=['DELETE'])
def builds_delete():
    for build in Builds:
        if build['id'] == int(id):
            Builds.remove(build)
    return "Success: Build Removed"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)