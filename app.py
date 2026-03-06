from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load knowledge base
with open("knowledge.json", "r") as file:
    knowledge = json.load(file)


from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("question", "").lower()

    if user_input == "help":
        topics = ", ".join(knowledge.keys())
        return jsonify({"answer": f"I can help with: {topics}"})

    for issue, solution in knowledge.items():
        if issue in user_input:
            return jsonify({"answer": solution})

    return jsonify({"answer": "Sorry, I don't know that issue yet."})


if __name__ == "__main__":
    app.run(debug=True)