name = input("What is your name? ")

# If length of name is greater than 20,
# print something

if len(name) > 20:
    print("Why can't your name be short and sweet, like 'pyra'?")

age = int(input("What is your age? "))

# If age is less than 10, print "Smol"
# ELse if age is between 10 and 20, print "Big boi"
# Else, print "Big big boi"

if age < 10:
    print("Congrats! You're younger than pyra!")
elif age > 10 and age < 20:
    print("Congrats! You're close to being pyrya's age!")
else:
    print("Congrats! You're older than pyra!")

coolness = float(input("Rate your coolness out of 100.0"))

# If coolness is more than 100.0, just print some error

if coolness > 100.0:
    print("Lies. You can't be cooler than pyra!")

# Now print a string like
# My name is Arnold Tan, I am 69 and I'm Really Cool

print("My name is pyra, I am a weeb and I love anime.")
