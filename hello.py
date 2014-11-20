from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

@app.route("/env")
def env():
	return MONGO_URL

if __name__ == "__main__":
	app.run()

