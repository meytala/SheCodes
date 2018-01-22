##function is composed of 3 elements:
# 1. the word def
# 1. the name of the function (that we assign
# 1. the parameters the function require

# 2. a comment that describe the functin

#3. the body - describe the procedure the functio does
#   the body is indendent


#First, def a function called cube that takes an argument called number. Don't forget the parentheses and the colon!
#Make that function return the cube of that number (i.e. that number multiplied by itself and multiplied by itself once again).
#Define a second function called by_three that takes an argument called number.
#if that number is divisible by 3, by_three should call cube(number) and return its result. Otherwise, by_three should return False.

def cube(number):
  return number**3

def by_three(number):
  if number%3==0:
    return cube(number)
  else:
    return False

print ("the answer to by_three function is:{}".format(by_three(3)))

##importing modules
#import math
#print math.sqrt(25)


#It's possible to import only certain variables or functions from a given module.
# Pulling in just a single function from a module is called a function import, and it's done with the from keyword:
# from module import function
#from math import sqrt

#Universal import - brings all the variables from the module
#from module import *

##to see what is there in a module:
#import math # Imports the math module
#everything = dir(math) # Sets everything to a list of things from math
#print everything # Prints 'em all!


maximum = max(1,2,3)
print (maximum)

minimum = min(1,2,3)
print (minimum)

absolute = abs(-42)
print (absolute)


def shut_down(s):
  if s == "yes":
    return "Shutting down"
  elif s == "no":
    return "Shutdown aborted"
  else:
    return "Sorry"


  def distance_from_zero(num):
	if type(num) == int or type(num) == float:
  		return abs(num)
  	else:
    		return "Nope"



