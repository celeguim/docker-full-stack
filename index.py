import requests
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    import socket
    ipaddr = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
    return "Hello World!" + "<br>" + ipaddr


@app.route("/cities")
def get_cities():
    response = requests.get(url="http://0.0.0.0:8081/api/cities")
    return response.text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
