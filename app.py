from flask import Flask
from flask import redirect, render_template, request, session

import search
import random

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("home.html")
    
    q = request.form.get('query', '')
    results = search.answer(q)
    return render_template("home.html". results = results)

@app.route("/waldo")    
def waldo():
    ## randomly select an image with waldo puzzle
    file_num = random.randrange(9) + 1
    img = "waldo_"+ str(file_num) + ".jpg"
    print img
    return render_template("waldo.html", img = img)

    
if __name__ == '__main__':
  app.debug = True
  app.run()
