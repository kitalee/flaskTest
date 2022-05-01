from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
import inspect

app = Flask(__name__)
api = Api(app)

names = {"daniel": {"age": 40, "gender": "male"}, "liz": {"age": 30, "gender": "female"}}

# Resource 상속
class HelloWorld(Resource):
    def get(self, name):
        return names[name]
    # def get(self, name, age):
    #     return {"name": name, "age": age}
    def post(self):
        return {"data": "Posted"}

api.add_resource(HelloWorld, "/helloworld/<string:name>")        
# api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:age>")        

# You need to add the location information to the RequestParser by default it tries to parse values from flask.Request.values, and flask.Request.json, but in your case, the values need to be parsed from a flask.request.form. 
# https://stackoverflow.com/questions/71794902/issue-with-bad-request-syntax-with-flask
videoPutArgs = reqparse.RequestParser()
videoPutArgs.add_argument("name", type=str, help="Need name of the video", location='form', required=True)
videoPutArgs.add_argument("views", type=int, help="Need views of the video", location='form', required=True)
videoPutArgs.add_argument("likes", type=int, help="Need likes on the video", location='form', required=True)

videos = {}

def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message="video id is not valid")

def abort_if_video_exists(video_id):
    if video_id in videos:
        abort(409, message="video already exists with that id")

class Video(Resource):
    def get(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id]

    def put(self, video_id):
        abort_if_video_exists(video_id)
        args = videoPutArgs.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        del videos[video_id]
        return '', 204


api.add_resource(Video, "/video/<int:video_id>")        

if __name__ == "__main__":
    # 모듈위치 확인
    print(inspect.getfile(Flask))
    app.run(debug=True)
    # app.run(debug=True, ssl_context="adhoc")