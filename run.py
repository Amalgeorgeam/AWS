
from flask import Flask, render_template, request
from app.bot import main_trading_logic

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/trade", methods=["POST"])
def trade():
    result = main_trading_logic()
    return result

if __name__ == "__main__":
    app.run(debug=True)
