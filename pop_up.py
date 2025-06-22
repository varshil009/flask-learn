from flask import Flask, url_for, redirect, request, flash, render_template

app = Flask(__name__)
app.secret_key = "one2three"
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods = ["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form['username'] == 'admin' or request.form['password'] == 'admin':
            error = "invalid username or password please try again !"
        
        else:
            flash("you successfully logged in")
            return redirect(url_for('index'))

    return render_template('login.html', error = error)

if __name__ == "__main__":
    app.run(debug = True)