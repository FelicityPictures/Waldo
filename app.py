from flask import Flask
from flask import redirect, render_template, request, session

import new_search
import random, string

app = Flask(__name__)

@app.route("/", methods=['GET'])
@app.route("/home", methods=['GET'])
@app.route("/home/", methods=['GET'])
def home():
    return render_template("home.html")


@app.route("/waldo", methods=['POST'])    
def waldo():
    q = request.form.get('query', '')
    results = new_search.search(q)
    #results = ["hi", "hi", "hi", "hi", "hi"]
    return render_template("waldo.html", results = results, query = string.capwords(q) )
    
if __name__ == '__main__':
  app.debug = True
  app.run(host="0.0.0.0", port=8000)
