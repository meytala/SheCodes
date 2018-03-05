###endless recursion
# def test (num):
#     num = test (num +1)
#     return num
# test (1)


#Question 6: In sum...
#Write a function sum that takes a single argument n and computes the sum
# of all integers between 0 and n inclusive. Assume n is non-negative.

print ("questin 6")
def sum (n):
    if n==0:
        return 0
    else:
        return (n+sum(n-1))

print (sum(8))

print ("questin 7")

#Return the sum of every other natural number up to n, inclusive".

def sum_every_other_number(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return n + sum_every_other_number(n - 2)

print(sum_every_other_number(9))

print ("questino 7 fibbonaci")
##1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 , 34 , 55 , 89 , 144

def fibonacci(n):
    if n == 1:
       return 1
    elif n == 2:
       return 1
    else:
       return fibonacci(n - 1) + fibonacci(n - 2)

print (fibonacci (11))


print ("question 8:")
#For the hailstone function from homework 1, you pick a positive integer n as the start.
# If n is even, divide it by 2.
# If n is odd, multiply it by 3 and add 1.
# Repeat this process until n is 1.
# Write a recursive version of hailstone that prints out the values of the sequence and returns the number of steps.

#    """Print out the hailstone sequence starting at n, and return the
#     number of elements in the sequence.
#
#     >>> a = hailstone(10)
#     10
#     5
#     16
#     8
#     4
#     2
#     1
#     >>> a
#     7
#     """

x=0

def hailstone (n):
    global x
    x+=1
    print (int(n))
    if n==1:
        return print("The number of steps is", x)
    elif n%2==0:
        n= n/2
        hailstone (n)
    else:
        n=(n*3)+1
        hailstone (n)


hailstone (10)


print ("question number 9:")
# Question 9: I Heard You Liked Functions...

# Define a function cycle that takes in three functions f1, f2, f3, as arguments.
# cycle will return another function that should take in an integer argument n and return another function.
# That final function should take in an argument x and cycle through applying f1, f2, and f3 to x,
# depending on what n was.
#
# Here's the what the final function should do to x for a few values of n:
#
# n = 0, return x
# n = 1, apply f1 to x, or return f1(x)
# n = 2, apply f1 to x and then f2 to the result of that, or return f2(f1(x))
# n = 3, apply f1 to x, f2 to the result of applying f1, and then f3 to the result of applying f2, or f3(f2(f1(x)))
# n = 4, start the cycle again applying f1, then f2, then f3, then f1 again, or f1(f3(f2(f1(x))))
# And so forth.

# def add1(x):
#     return x + 1
# def times2(x):
#     return x * 2
# def add3(x):
#     return x + 3
#
#
# def cycle (add1, times2, add3):

print ("additional Q")


print ("Q1:")
#. Write a function that takes in two numbers and recursively multiplies them together

def multiply(x, y):
    if y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + multiply(x, y - 1)

print (multiply (4, 3))


print ("Q2:")

#2. Write a function that takes in a base and an exp and recursively computes baseexp. You are not allowed to
#use the ** operator

def base_exp (x,y):
    if y==0:
        return 1
    else:
        return x * base_exp (x, y-1)

print (base_exp (4, 3))

print ("Q3:")
#3. Write a function using recursion to print numbers from n to 0

def num_to_zero (n):
    print (n)
    if n == 1:
        return 0
    else:
        return num_to_zero (n-1)

print (num_to_zero (5))
