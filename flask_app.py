from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
	return 'Hello, World! Sachin... Stay Home. Stay Safe.'
    # name = request.args.get("name", "World")
    # return f'Hello, {escape(name)}!'