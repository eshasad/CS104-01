#CS104
#Esha Asad
#Conditions.py

# Input temperature from the user
temp = int(input("Please enter the current temperature: "))

# Check temperature conditions and provide appropriate advice
if temp > 90:
    print("Wear Shorts")
elif temp > 70:
    print("Short sleeves are fine")
elif temp > 50:
    print("Wear a jacket")
elif temp > 32:
    print("Wear a heavy coat")
else:
    print("Stay Inside")
