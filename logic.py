def get_diet_plan(age, height, weight, activity, gender):
    height_m = height / 100
    bmi = round(weight / (height_m ** 2), 1)

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
        diet = "Low-fat, high-fiber foods"
        risk = "Risk of lifestyle diseases"

    if gender == "female":
        diet += ", iron-rich foods (spinach, jaggery)"
    else:
        diet += ", strength-supporting foods"

    return {
        "bmi": bmi,
        "status": status,
        "diet": diet,
        "risk": risk
    }
