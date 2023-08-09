from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

budgets = {"League-Starter": {"RF Inquisitor": "pastebin.URL", "Boneshatter Juggernaut": "pastebin.URL"},
           "MidRange": {"Impending Doom Pathfinder": "pastebin.URL"}}

class BuildTypes(Resource):
    def get(self, budget):
        return budgets[budget]
    
api.add_resource(BuildTypes, "/buildtypes/<string:budget>")

if __name__ == "__main__":
    app.run(debug=True) 