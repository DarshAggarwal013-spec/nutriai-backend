def get_diet_plan(bmi):
    bmi = float(bmi)

    if bmi < 18.5:
        return {
            "status": "Underweight / कम वजन",
            "diet": "दाल, दूध, मूंगफली जैसे उच्च प्रोटीन भोजन",
            "risk": "कुपोषण का खतरा"
        }
    elif bmi < 25:
        return {
            "status": "Healthy / स्वस्थ",
            "diet": "रोटी, सब्ज़ी, फल वाला संतुलित आहार",
            "risk": "कम स्वास्थ्य जोखिम"
        }
    else:
        return {
            "status": "Overweight / अधिक वजन",
            "diet": "कम चीनी, अधिक फाइबर भोजन",
            "risk": "जीवनशैली रोगों का खतरा"
        }

  style="font-size:12px;color:gray;">
" NutriAI provides general wellness guidance and is not a medical diagnosis tool."
 


