# BMI CALCULATOR

print('''=== BMI CALCULATOR ===
''')

# Input height in feet
height_ft = float(input("Height in ft: "))

# Input weight in kg
weight = float(input("Weight in Kg: "))

# Convert height feet to m (1ft = 0.3048)
height_m = height_ft * 0.3048

# Calculate BMI
bmi = weight / (height_m ** 2)

# Show BMI value
print(f"\nYour BMI is: {bmi:.2f}")

# Check BMI category
if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal Weight")       
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: OBESE")

#end