def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)


def fitness_plan(bmi, age):

    if bmi < 18.5:
        return {
            "category": "Underweight",
            "steps": "6000 steps/day",
            "workout": "Light strength training + yoga",
            "diet": "High protein diet, nuts, milk, eggs"
        }

    elif 18.5 <= bmi < 25:
        return {
            "category": "Normal",
            "steps": "8000 steps/day",
            "workout": "Cardio + bodyweight training",
            "diet": "Balanced diet with protein and vegetables"
        }

    elif 25 <= bmi < 30:
        return {
            "category": "Overweight",
            "steps": "10000 steps/day",
            "workout": "Cardio, HIIT, cycling",
            "diet": "Low carb, high fiber diet"
        }

    else:
        return {
            "category": "Obese",
            "steps": "12000 steps/day",
            "workout": "Walking, light cardio",
            "diet": "Calorie deficit diet, avoid sugar"
        }
