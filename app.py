from flask import Flask, request, jsonify
from logic import get_diet_plan

app = Flask(__name__)

@app.route("/diet", methods=["POST"])
def diet():
    data = request.json
    bmi = data["bmi"]
    plan = get_diet_plan(bmi)
    return jsonify(plan)

if __name__ == "__main__":
    app.run(debug=True)
@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json["message"].lower()

    if "diet" in msg or "खाना" in msg:
        reply = "Balanced Indian diet includes roti, dal, sabzi, fruits."
    elif "anemia" in msg or "खून" in msg:
        reply = "Iron-rich foods include spinach, jaggery, lentils."
    elif "diabetes" in msg or "शुगर" in msg:
        reply = "Reduce sugar, eat whole grains, and exercise daily."
    else:
        reply = "Please consult a healthcare professional for medical advice."

    return jsonify({"reply": reply})
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>NutriAI Backend is Live</h1>
    <p style="font-size:12px;color:gray;">
        NutriAI provides general wellness guidance and is not a medical diagnosis tool.
    </p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)







