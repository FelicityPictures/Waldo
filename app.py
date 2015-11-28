from flask import Flask
from flask import redirect, render_template, request, session

import new_search
import random

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("home.html")
    
    q = request.form.get('query', '')
    results = new_search.search(q)
    return render_template("home.html", results = results)

@app.route("/waldo")    
def waldo():
    ## randomly select an image with waldo puzzle
    file_num = random.randrange(9) + 1
    img = "waldo_"+ str(file_num) + ".jpg"
    return render_template("waldo.html", img = img)

    
if __name__ == '__main__':
  app.debug = True
  app.run(host="0.0.0.0", port=8000)
