from flask import Flask

app = Flask(__name__)

@app.route('/') #home or root of website
def index():
    return '<html><head><title>Hello World!</title></head><body><h1>hello world</h1><p> Ir a <a href="/about">About</a></p></body></html>'

@app.route('/about') #info about this site
def about():
    return '<html><head><title>About this page</title></head><body>Everything about this website. Back to <a href="/">Hello world</a></body></html>'

if __name__ == '__main__':
    app.run(debug=True)