from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

app2 = Flask(__name__)
app = app2

# @app.route("/")
# def hello_world():
#     return "<h1>Hello, World!</h1>"
@app.route("/", methods=['GET'])
def homepage():
    return render_template("index.html")


if __name__ == "__main__":
    # app.run(host="0.0.0.0")
    app.run(host="127.0.0.1")