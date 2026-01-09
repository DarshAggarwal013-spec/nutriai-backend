from flask import Flask, request, jsonify
from flask_cors import CORS
from logic import get_diet_plan

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "NutriAI backend is running"

@app.route("/diet", methods=["POST"])
def diet():
    try:
        data = request.get_json()

        age = int(data["age"])
        height = float(data["height"])
        weight = float(data["weight"])
        activity = data["activity"]
        gender = data["gender"]

        result = get_diet_plan(age, height, weight, activity, gender)
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
