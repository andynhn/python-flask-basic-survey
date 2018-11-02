# By Andy Nguyen

from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=['POST'])
def submitSurvey():
    print(request.form)
    print("Name", request.form["name"])
    print("Dojo Location", request.form["dojo_location"])
    print("Favorite Language", request.form["favorite_language"])
    print("Comment", request.form["comment"])
    return render_template("result.html")

@app.route("/danger")
def danger():
    print("DANGER: A user tried to visit /danger. We have redirected the user to /")
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)

# Build a flask application that accepts a form submission and presents the submitted data on a results page.
# The goal is to help you get familiar with sending POST requests through a form and displaying that information. 
# http://localhost:5000 - have this display a nice looking HTML form.  The form should be submitted to '/result'
# http://localhost:5000/result - have this display a html with the information that was submitted by POST
# http://localhost:5000/danger - have this redirect back to "/".  Before redirecting back print in the terminal/console a message: "a user tried to visit /danger.  we have redirected the user to /".