from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

@app.route("/")
def renderStartingPage():
    r = requests.get("http://localhost:3000/college/api/v1.0/getCollegeList")
    data = r.json()
    #print(data["data"][0])
    return render_template("./index.html", data = data, )

if __name__ == "__main__":
    app.run()
