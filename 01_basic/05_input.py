# The input() function is used to ask the user for information while the program is running.
# Here, I ask for the user's name and save their answer inside a variable.
# Adding a line break (\n) at the end makes the user type on the next line instead of right next to the question:
name = input("Hi, what's your name?\n")
print(f"Nice to meet you, {name}")

# Something important to clarify is that input() ALWAYS saves the user's answer as a str (text).
# So if we want to build a calculator or do math, we need to convert it into an int or float first
# (just like we learned in the Type Casting section):
age = int(input("Hi, how old are you?\n"))
print(f"In 5 years, you will be {age + 5} years old!")

# Just like we did with variables earlier, if you want to get multiple inputs at once,
# you can add .split() at the end of input().
# By default, .split() separates the user's answer wherever there is a space:
first_name, last_name = input("Enter your first and last name (separated by a space):\n").split()
print(f"First name: {first_name}, Last name: {last_name}")

# exercises
# Now use input(), casting (int/float), f-strings, and .split() to solve these exercises:
# 1. Ask the user for their favorite city using input() and print a message using an f-string
#    (for example: "Awesome, I would love to visit {city} too!").
# 2. Build a mini addition calculator: ask the user for two whole numbers (using int(input(...)))
#    and print the result of adding them together.
# 3. Ask the user for their weight in kg (as a float) and their height in meters (as a float),
#    then calculate their BMI using: weight / (height * height).
# 4. Use .split() on a single input() to ask for their favorite color and favorite animal
#    separated by a space, then print both inside a sentence.
# 5. First, answer this question in your head: if you run num = input("Enter a number: ") and then
#    print(num * 3) typing "5", will Python print 15 or "555"?
# 6. Run it to check your answer and remember why casting input() data is so important

# If you get stuck, scroll up, check the examples, and try again.
# Congratulations 👏🎉 You finished the fifth part and the first section of my tutorial 
# Congrats🎉 you officially graduated from knowing nothing to knowing a little something🎓