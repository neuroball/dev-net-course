"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print("{_type} {_value}".format(_type=type(pi), _value=pi))

# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if (i < 50):
  print("i is less than 50. i is {}".format(i))
elif (i > 50):
  print("i is greater than 50. i is {}".format(i))
else:
  print("i is equal to 50. i is {}".format(i))


# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
if (picked_fruit == 'orange'):
  print("You're an orange, Harry!")
elif (picked_fruit == 'strawberry'):
  print("You are as red as a strawberry!")
elif (picked_fruit == 'banana'):
  print("You do the banana mash!")

# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def multiply(num1, num2):
  return num1 * num2


# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 = {}".format(multiply(12, 96)))

print("48 x 17 = {}".format(multiply(48, 17)))

print("196523 x 87323 = {}".format(multiply(196523, 87323)))

