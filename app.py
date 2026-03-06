from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load knowledge base
with open("knowledge.json", "r") as file:
    knowledge = json.load(file)


@app.route("/")
def home():
    return "DevOps Troubleshooting Bot API is running!"


@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("question", "").lower()

    for issue, solution in knowledge.items():
        if issue in user_input:
            return jsonify({"answer": solution})

    return jsonify({"answer": "Sorry, I don't know that issue yet."})


if __name__ == "__main__":
    app.run(debug=True)