# BMI Calculator

def calculate_bmi(Weight, Height):
    bmi = Weight / (Height**2)
    return bmi

def classify_bmi(bmi):
    if bmi<18.5:
        return "Underweight"
    elif bmi<25:
        return "Normal"
    elif bmi<30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator!")

    Weight = float(input("Enter your Weight (in kilogram): "))
    Height = float(input("Enter your Height (in meters): "))

    bmi = calculate_bmi(Weight, Height)
    category = classify_bmi(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"Your BMI category is: {category}")

main()


                        
                        
    
