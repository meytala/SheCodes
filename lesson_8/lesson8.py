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
