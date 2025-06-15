from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <body>
            <form action="/login" method="get">
                <p>Enter Name:</p>
                <p><input type="text" name="name" /></p>
                <p><input type="submit" value="Submit" /></p>
            </form>
        </body>
    </html>
    '''

@app.route('/success/<name>')
def success(name):
    return f"Welcome {name}!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['name']
    else:
        user = request.args.get('name')
    return redirect(url_for('success', name=user))

if __name__ == "__main__":
    app.run(debug=True)
