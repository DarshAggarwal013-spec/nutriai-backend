from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/diet", methods=["POST"])
def get_diet():
    data = request.json

    age = int(data["age"])
    height_cm = float(data["height"])
    weight = float(data["weight"])
    activity = data["activity"]
    gender = data.get("gender", "male")  # default safe

    height_m = height_cm / 100
    bmi = round(weight / (height_m ** 2), 1)

    # ---- CHILD LOGIC ----
    if age < 18:
        return jsonify({
            "bmi": bmi,
            "status": "Child BMI varies by age & gender",
            "note": "BMI-for-age percentile required",
            "risk": "Consult pediatric guidelines"
        })

    # ---- ADULT LOGIC ----
    if bmi < 18.5:
        status = "Underweight"
        diet = "High-protein foods like dal, milk, peanuts"
        risk = "Risk of malnutrition"

    elif bmi < 25:
        status = "Normal"
        diet = "Balanced Indian diet"
        risk = "Low risk"

    else:
        status = "Overweight"
        diet = "Low sugar, more vegetables"
        risk = "Risk of lifestyle diseases"

    # Gender-based note
    if gender == "female":
        diet += ", iron-rich foods recommended"

    return jsonify({
        "bmi": bmi,
        "status": status,
        "diet": diet,
        "risk": risk
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
