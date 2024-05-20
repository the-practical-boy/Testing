from flask import Flask
from flask import request as req
app=Flask(__name__) # Object of Flask

@app.route('/')
def hello_world():
    return "<h1> Hello World </h1>"

@app.route('/seed')
def hello_world1():
    return "<h1> Hello Billi </h1>"

@app.route('/seed2')
def hello_world2():
    return "<h1> Hello Mausi </h1>"

@app.route('/test')
def test():
    return "This is my function to return the statement {}".format(5+6)

@app.route('/test2')
def test2():
    data=req.args.get('key')
    return "this is my function to return input data {}".format(data)


if __name__=='__main__':
    app.run(host='0.0.0.0')


''' @app.route('/abc') means that you are connecting to the server url having /abc at the end '''
