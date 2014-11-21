from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

@app.route("/env")
def env():
	return os.getenv("MONGO_URL", "tralal")

@app.route("/nino")
def nino():
	return "ja sam nino!"

if __name__ == "__main__":
	app.run()

