def bmi_calculator(height, weight):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "Normal weight"
    else:
        return "Overweight"

while True:
    height = input("Enter your height (m): ")
    if height == "off":
        break
    height = float(height)

    weight = input("Enter your weight (kg): ")
    if weight == "off":
        break
    weight = float(weight)

    result = bmi_calculator(height, weight)
    print("Your body mass index is: ", result)
