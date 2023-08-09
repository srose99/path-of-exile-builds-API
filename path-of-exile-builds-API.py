from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

build_put_args = reqparse.RequestParser()
build_put_args.add_argument("Name", type=str, help="Name of the build is required", required=True)
build_put_args.add_argument("Budget", type=str, help="I.E League-Starter, MidRange, HighEnd is required", required=True)
build_put_args.add_argument("Pastebin", type=str, help="pastebin link for the builds POB details is required", required=True)
build_put_args.add_argument("Description", type=str, help="Short description of the build, its strengths and weaknesses is required", required=True)

#Builds need a: Name, Budget, Pastebin, Description
builds = {}

class Builds(Resource):
    def get(self, build):
        return builds[build]
    def put(self, build):
        args = build_put_args.parse_args()
        builds[build] = args
        return builds[build], 201
    
api.add_resource(Builds, "/builds/<string:build>")

if __name__ == "__main__":
    app.run(debug=True) 