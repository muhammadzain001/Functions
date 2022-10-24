#  reuse code on different variables and values without
# having to rewrite it would save you significant amounts of time and allow you to use much less code

def function_name():
    print(2 + 2)


function_name()


# a parameter is a placeholder name for the variable or data that you want your function to run its code

def name(parameter):
    print(parameter + 2)


name(8)

# multiple parameters

first_str = "the number"


def var(p1, p2, p3):
    print(p1 + str(p2) + p3)


var(first_str, 5, " is an integer")


# default strings

def example(num1=7, num2=8):
    print(num1 * num2)


example()


# in the example above it takes reading from default perimeters


def example(num1=7, num2=8):
    print(num1 * num2)


example(2)


# in the example above it replaces the default value of num1 with 2

# ================================================================================================
def def_example(num=7, num0=8):
    return num * num0


print(def_example() + 44)


# ================================================================================================

def hello_world_printer():
    print("hello world")


hello_world_printer()


# =================================================================================================

def name_printer(user_name):
    print(user_name)


name = input("please enter your name")
name_printer(name)

# ==================================================================================================
# Programming Exercise

length = int(input("Please enter the length of ur rectangle "))
width = int(input("Please enter the width of ur rectangle "))
height = int(input("Please enter the height of ur rectangle "))


def rectangleinput(l, w, h):
    return l * w * h


print("the volume of the rectangular prism is " + str(rectangleinput(length, width, height)) + " cubic feet")


# =====================================================================================================

celsius = int(input("Enter your celsius integer. "))

# To avoid the approximation error that would occur if the float 1.8 was used in the calculation, 1.8 * 10 is used
    # instead, resulting in the integer 18.  To balance this out, 32 is also multiplied by 10 to get 320.  After the
    # calculations in the parentheses are finished, the result is divided by 10, which gives the correct Fahrenheit
    # temperature.

def fahrenheit(cel):
    return (18 * cel + 320) / 10
print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(fahrenheit(celsius)) + " F .")
