from flask import Flask
from logbook import Logger
from api import DataGatherView, GraphView

app = Flask(__name__)
log = Logger(__name__)

DataGatherView.register(app, route_base="/i/")
GraphView.register(app, route_base="/g/")

if __name__ == "__main__":
    app.run(debug=True)