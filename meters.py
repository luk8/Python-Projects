#Constant define for meter to feet and yard

METER_TO_FEET = 3.28
METER_TO_YARD = 1.09

# User input the distance in meters

userInput = input("Please enter the distance in meters: ")
distance = float(userInput)

#Convert meters in feet and yards

FEET = distance * METER_TO_FEET
YARDS = distance * METER_TO_YARD

# Print distance in feet and yards

print("The distance in feet is %.2f" % FEET)
print("The distance in yards is %.2f" % YARDS)
