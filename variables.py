from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
   return f'Hello {name}!' 

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

@app.route('/flask')
def hello_flask():
   return 'Hello Flask'

@app.route('/python/')
def hello_python():
   return 'Hello Python'

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

# if name is 'admin', redirect to hello_admin
# if name is anything else, redirect to hello_guest with the name as guest
# we make a new address take var and redirect to appropriate address using redirect and url_for
@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest', guest = name))


if __name__ == '__main__':
   app.run(debug = True)    