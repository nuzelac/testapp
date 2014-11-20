from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

@app.route("/env")
def env():
	return os.getenv("MONGODB_URL", "tralal")

if __name__ == "__main__":
	app.run()

