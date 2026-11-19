# Type casting or type converion.
# Type casting is used when we need to switch the data type of a value into another one.
# For example, turning text that looks like a number ("10") into an actual number (10) so we can do math with it.

# For this, we are going to use the data types we already know, like str, int, float, and bool.
# We use them as commands with parentheses around what we want to convert, like this: datatype("value_to_convert")
print(type(int("10")))
 
# This is useful when we are using incompatible types:

# Doesn't work (because "10" is a str, not an int):
# print("10" + 5)

# Works:
print(int("10") + 5)

# This works differently depending on the situation.
# For example, if you convert a float to an int, Python doesn't round it; it just removes the numbers after the decimal point:
print(int(10.9))

# If you want to round a number, there is a command called round().
# Interestingly, when a number ends in .5, Python rounds it to the nearest even number:
print(round(2.5))  # = 2
print(round(3.5))  # = 4
print(round(2.50000000000001)) # = 3 (because it's > .5)

# In booleans, nothing (empty) or 0 is False, and the rest is True:
print(bool(""))
print(bool(0))

print(bool("hi"))
print(bool(-1))

# You can't convert a string with letters (like "hello") into an int or a float:
# print(int("hello"))

# exercises
# Now use print(), type(), round(), and casting functions to solve these exercises:
# 1. Print the result of adding "20" (a str) and 5 (an int) by converting "20" into an integer first.
# 2. Convert the float 7.99 into an int, and then use round() on 7.99 to see the difference between both results.
# 3. Print the phrase "My age is 16" by combining "My age is " + 16, using str() so Python doesn't give you an error.
# 4. Check the data type of str(16) using type() to confirm it is now text.
# 5. First, answer this question: if you run print(int("python")), will it convert the text or crash with an error?
# 6. Run it (and then comment it out with #) to see what happens in real life when you try to convert letters into a number.

# If you get stuck, scroll up, check the examples, and try again.
# Congratulations 👏🎉
# You finished the third part of my tutorial.
# Next up: variables
