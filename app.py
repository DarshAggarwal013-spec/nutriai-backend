from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# ----------------------------
# Home route (for testing)
# ----------------------------
@app.route("/")
def home():
    return "NutriAI backend is live."

# ----------------------------
# Diet API
# ----------------------------
@app.route("/diet", methods=["POST"])
def diet():
    data = request.get_json()
    bmi = float(data.get("bmi", 0))

    if bmi < 18.5:
        result = {
            "status": "Underweight / कम वजन",
            "diet": "High-protein foods like dal, milk, peanuts",
            "risk": "Risk of malnutrition"
        }
    elif bmi < 25:
        result = {
            "status": "Healthy / स्वस्थ",
            "diet": "Balanced Indian diet with roti, sabzi, fruits",
            "risk": "Low health risk"
        }
    else:
        result = {
            "status": "Overweight / अधिक वजन",
            "diet": "Low sugar, high fiber foods like vegetables and oats",
            "risk": "Risk of lifestyle diseases"
        }

    return jsonify(result)

# ----------------------------
# Chatbot API
# ----------------------------
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "").lower()

    if "diet" in message or "food" in message or "खाना" in message:
        reply = "A balanced diet includes roti, dal, vegetables, fruits, and water."
    elif "anemia" in message or "खून" in message:
        reply = "Iron-rich foods include spinach, jaggery, dates, and lentils."
    elif "diabetes" in message or "sugar" in message:
        reply = "Reduce sugar intake and prefer whole grains and vegetables."
    else:
        reply = "This is general wellness advice. Please consult a doctor for medical concerns."

    return jsonify({"reply": reply})

# ----------------------------
# Render-required runner
# ----------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
