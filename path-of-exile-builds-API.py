from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class BuildTypes(Resource):
    def get(self):
        return {"Tanky", "Fast", "Hybrid"}
    
api.add_resource(BuildTypes, "/buildtypes")

if __name__ == "__main__":
    app.run(debug=True)