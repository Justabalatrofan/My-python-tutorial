# Variables are one of the most important things in Python.
# Variables work to store information or assign a value.

# To assign a value to a variable, it looks like this:
my_first_variable = "is this"

# And now it has the assigned value:
print(my_first_variable)
# = is this

# Variables can also be reassigned:
my_first_variable = "another value"

# And now the variable changes:
print(my_first_variable)
# = another value

# Something important about variables is that Python uses dynamic typing.
# In short, you don't need to declare the variable's type,
# and its type can change during runtime (while the program is running):
print(type(my_first_variable))
# = <class 'str'>

my_first_variable = 100
print(type(my_first_variable))
# = <class 'int'>

# Another important thing is that Python is strongly typed.
# In other words, it doesn't do automatic type conversions.
# Just like when we tried to add an int or float with a str (which causes an error):
# print(10 + "5")

# A great feature for using variables inside text is f-strings.
# They work by placing an f before the quotes and putting variables or expressions inside curly braces {}:
print(f"Hi, I am {my_first_variable - 99} year old")
# = Hi, I am 1 year old

# Something else you can do—though in my opinion I don't recommend it because it looks messy—
# is assign multiple variables at once.
# You do this by separating the variables and values with commas:
number_1, number_2, number_3 = 2, 9, 11
print(number_1, number_2, number_3)
# = 2 9 11

# VARIABLE NAMING RULES 

# What not to do
# You can't start a variable name with a number:
# 1name = "jorge"  

# You also can't use Python's reserved keywords as variable names:
# ['False', 'None', 'True', 'and', 'as', 'assert',
# 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import', 'in', 'is',
# 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']

# You also can't use spaces or hyphens (-), and don't forget quotes around strings:
#  my name = "jorge"  
# my-name = "jorge"  

# Correct way (using underscores / snake_case):
name_1 = "jorge"

# Because Python is dynamically typed, it doesn't have strict constants
# or strict variable types. You can only leave "hints" for other programmers:

# 1. Type hints (just a note—Python won't enforce it when running):
variable: bool = 1
print(variable)        # = 1
print(type(variable))  # = <class 'int'> (even though we wrote ": bool", it's still an int)

# 2. Constants (written in ALL_CAPS by convention so others know not to change them):
PI = 3.1416
# Python will still let you change PI if you try, so it relies on programmer discipline!

# exercises
# Now use variables, f-strings, type hints, and constants to solve these exercises:
# 1. Create a variable called favorite_food with your favorite food (a str) and print it.
# 2. Reassign favorite_food to a different food and print it again to see how its value changes.
# 3. Create a variable for your age and use an f-string to print: "Next year I will be [age + 1] years old".
# 4. Create a constant called MAX_LIVES with the value 3 (remember the naming convention).
# 5. First, answer this question in your head: if you write test_var: str = 50 and print(type(test_var)),
#    will Python print <class 'str'> or <class 'int'> ?
# 6. Run it to check your answer and see how type hints really work in Python.
# 7. Spot the errors! Why are these variable names invalid? (Don't run them, just explain it to yourself):
#    - 2nd_player = "Alex"
#    - global = True
#    - user-score = 100

# If you get stuck, scroll up, check the examples, and try again.
# Congratulations 👏🎉 You finished the fourth part of my tutorial
# Next up: Input fuction
