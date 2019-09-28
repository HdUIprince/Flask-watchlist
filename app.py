from flask import Flask
from flask import url_for

app = Flask(__name__)

@app.route('/')
# @app.route('/home')
# @app.route('/index')
def hello():
    # return 'Welcome to My watchlist!'
    # return u'欢迎来到我的Watchlist!'
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/user/<name>')
def user_page(name):
    return f'<h1>User {name}</h1>'

@app.route('/test')
def test_url_for():
    # get relate URL
    print(url_for('hello'))
    print(url_for('user_page', name='greyli'))
    print(url_for('user_page', name='peter'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2))
    return 'Test Page'
