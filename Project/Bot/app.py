
from flask import Flask, request, render_template, jsonify
from gpt_strategy import analyze_market_input
from smartapi_helper import place_order

app = Flask(__name__)

# Store last GPT decision
gpt_decision = {}

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    global gpt_decision
    user_input = request.form.get("user_input")
    decision = analyze_market_input(user_input)
    gpt_decision = decision
    return jsonify(decision)

@app.route("/place_order", methods=["POST"])
def order():
    global gpt_decision
    if not gpt_decision:
        return jsonify({"error": "No decision available"}), 400
    result = place_order(gpt_decision)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
