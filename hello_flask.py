from flask import Flask
app = Flask(__name__)

@app.route('/')
def Hello_World():
    return 'Hello, Flask!'

@app.route('/about')
def about():
    return 'This is About Page'

@app.route('/contact')
def contact():
    return 'This is Contact Page'

if __name__ == '__main__':
    app.run()


"""
Decorators like @app.route('/') register the function (Hello_World() in this case) as a handler for a specific URL route ('/').
When you run app.run(), Flask:
Starts a built-in development web server.
Waits (listens) for HTTP requests from a browser or client.
Only when someone sends a request to '/', Flask looks up the registered function for that route (Hello_World) and executes it.

You start the server with app.run().
A browser sends a request to http://localhost:5000/.
Flask finds the matching route / and calls Hello_World().
The returned string 'Hello, Flask!' becomes the HTTP response sent back to the browser.

"""