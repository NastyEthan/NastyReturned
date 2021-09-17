# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/README/')
def README():
    return render_template("README.html")

@app.route('/name/')
def name():
    return render_template("name.html")

@app.route('/michael/', methods=['GET', 'POST'])
def michael():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("michael.html", name=name)
    # starting and empty input default
    return render_template("michael.html", name="World")

@app.route('/anirudh/', methods=['GET', 'POST'])
def anirudh():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("anirudh.html", name=name)
    # starting and empty input default
    return render_template("anirudh.html", name="World")

@app.route('/ethan/', methods=['GET', 'POST'])
def ethan():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:
            return render_template("ethan.html", name=name)
            # starting and empty input default
    return render_template("ethan.html", name="World")

@app.route('/james/', methods=['GET', 'POST'])
def james():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("james.html", name=name)
    # starting and empty input default
    return render_template("james.html", name="World")

@app.route('/minilab/', methods=['GET', 'POST'])
def minilab():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Minilab.html", name=name)
    # starting and empty input default
    return render_template("Minilab.html", name="World")

@app.route('/binary/', methods=['GET', 'POST'])
def binary():
    if request.form:
        bits = request.form.get("bits")
        if len(bits) != 0:  # input field has content
            return render_template("binary.html", bits=int(bits))
    #if request.form:
     #   static = request.form.get("img")
    # starting and empty input default
    return render_template("binary.html", bits=8)

@app.route('/About/')
def About():
    return render_template("About.html")

@app.route('/planner/')
def planner():
    return render_template("planner.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
