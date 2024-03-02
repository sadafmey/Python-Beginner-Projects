def calculate_bmi(weight, height):
  
    bmi = weight / (height ** 2)
    return bmi

def main():
    print("Welcome to the BMI Calculator!")
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is: {bmi:.2f}")

if __name__ == "__main__":
    main()
