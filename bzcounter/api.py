import json
import redis
from flask import render_template, request, jsonify
from flask.ext.classy import FlaskView, route

try:
    with open('/home/dotcloud/environment.json') as f:
        env = json.load(f)
        r = redis.Redis(password=env['DOTCLOUD_DATA_REDIS_PASSWORD'],
                        host=env['DOTCLOUD_DATA_REDIS_HOST'],
                        port=int(env['DOTCLOUD_DATA_REDIS_PORT']),
                        db=0)
except IOError:
    r = redis.Redis()


class DataGatherView(FlaskView):

    def index(self):
        return render_template('index.html')

    def post(self):
        print request.json
        r.set("tipples:{0}".format(request.json.get('createdAt')),
            request.json.get('drinks'))
        return 'OK', 200


class GraphView(FlaskView):
    def index(self):
        return "<br>".join("quotes")
