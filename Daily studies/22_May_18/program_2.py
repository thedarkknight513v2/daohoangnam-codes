# This is a program that will convert seconds into hours, minutes, and seconds
# written in May 2018 by DHN

seconds = int(input("Please enter seconds"))
print(seconds)

# Convert to hours
hours = seconds // 3600
seconds_remaining1 = seconds % 3600

# Convert to minutes
minutes = seconds_remaining1 // 60
seconds_remaining2 = seconds_remaining1 % 60

# Print the result
print("Result: ",hours," hours", minutes," minutes",seconds_remaining2," seconds")