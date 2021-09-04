from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


# @app.route("/")
# def index():
#     return render_template('index.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        name = request.form['username']
        age = request.form['age']
        location = request.form['location']
        email = request.form['email']

        user = {
            "name":name,
            "age": age,
            "location": location,
            "email": email,
        }

        # validation for password

        return render_template("welcome.html", content=user)
    
    return render_template('login.html')   


if __name__ == '__main__':
    app.run(debug=True)    