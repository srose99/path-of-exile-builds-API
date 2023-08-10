from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class BuildModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    budget = db.Column(db.String(100), nullable=False)
    pastebin = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Build(name = {name}, budget = {budget}, pastebin = {pastebin}, description = {description})"
    

build_put_args = reqparse.RequestParser()
build_put_args.add_argument("name", type=str, help="Name of the build is required", required=True)
build_put_args.add_argument("budget", type=str, help="I.E League-Starter, MidRange, HighEnd is required", required=True)
build_put_args.add_argument("pastebin", type=str, help="pastebin link for the builds POB details is required", required=True)
build_put_args.add_argument("description", type=str, help="Short description of the build, its strengths and weaknesses is required", required=True)

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'budget': fields.String,
    'pastebin': fields.String,
    'description': fields.String
}

class Builds(Resource):
    @marshal_with(resource_fields)
    def get(self, build):
        result = BuildModel.query.filter_by(id=build).first()
        if not result:
            abort(404, message="Couldnt be found")
        return result
    
    @marshal_with(resource_fields)
    def put(self, build):
        args = build_put_args.parse_args()
        result = BuildModel.query.filter_by(id=build).first()
        if result:
            abort(409, message="build id was taken already")
        build_data = BuildModel(id=build, name=args['name'], budget=args['budget'], pastebin=args['pastebin'], description=args['description'])
        db.session.add(build_data)
        db.session.commit()
        return build_data, 201
    
    @marshal_with(resource_fields)
    def patch(self,build):
        args = build_put_args.parse_args()
        result = BuildModel.query.filter_by(id=build).first()
        if not result:
            abort(404, message="Build does not exist, cannot update")

        if args['name']:
            result.name = args["name"]
        if args['budget']:
            result.budget = args["budget"]
        if args['pastebin']:
            result.pastebin = args["pastebin"]
        if args['description']:
            result.description = args["description"]
        
        db.session.commit()

        return result
    
    @marshal_with(resource_fields)
    def delete(self, build):
        abort_if_invalid(build)
        del builds[build]
        return "", 204
    
api.add_resource(Builds, "/builds/<string:build>")

if __name__ == "__main__":
    app.run(debug=True) 