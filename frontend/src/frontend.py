#Fontend

from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def call_backend():
    response = requests.get("http://backend-svc:5000")
    return f"Frontend got: {response.text}"

app.run(host="0.0.0.0", port=5000)
