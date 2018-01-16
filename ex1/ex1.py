###first exercise:
##given two int values, return their sum. Unless the two values are the same, then return double their sum.
##sum_double(1, 2) → 3
##sum_double(3, 2) → 5
##sum_double(2, 2) → 8'

def sum_double (x,y):
    if (x!=y):
        return (x+y)
    else:
        return (x+y)*2

x=sum_double (3,2)
print ("the answer to the first excercise is:")
print ('{} {}'.format("the answer to the function sum_double is ", x)) ###debugged - also work with other variables


##second excercise
##Given a string, return a new string where "not " has been added to the front.
## However, if the string already begins with "not", return the string unchanged.

#not_string('candy') → 'not candy'
#not_string('x') → 'not x'
#not_string('not bad') → 'not bad'

def not_string(word):
    print(word[0:3])
    if word[0:3] == "not":
        return word
    else:
        return ('{} {}'.format ("not",word))

y = not_string ('cat')
print ("the answer to the second excercise is:")
print (y)

##third excercise
##Given a non-empty string and an int n, return a new string where the char at index n has been removed.
# The value of n will be a valid index of a char in the original string
# (i.e. n will be in the range 0..len(str)-1 inclusive).

#missing_char('kitten', 1) → 'ktten'
#missing_char('kitten', 0) → 'itten'
#missing_char('kitten', 4) → 'kittn'


def missing_char (text, n):
    ##text=list(text)
    if n<=len(text):
        text = text[:n] + text[n+1:]
        return text
        #del text[n]

z= missing_char ('kitten', 1)
print ("the answer to the third excercise is:")
print (z)


##excersice 4
##Given a string, return a new string where the first and last chars have been exchanged.

# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'

def front_back(text):
    if len(text)>1:
        ##print(text[-1:])
        ##print(text[1:-1])
        ##print(text[0])
        return text[-1:] + text[1:-1] + text[0]
    else:
        return text

A = front_back('ab')
print ("the answer to the forth excercise is:")
print(A)


###fifth excersice - write a function that take a first name, last name and
  ##year of birth.
  ##calculate the person' age, and acroname
  ##your intials are X.Y. AND YOUR AGE IS xxxx

first_name = input ('enter your first name:')
last_name = input ('enter your last name:')
year_of_birth = input ('enter your year of birth:')

if  first_name.isalpha() and last_name.isalpha():
    fn = str(first_name)[0]
    ln = str(last_name)[0]
    bd = int(year_of_birth)
    import datetime
    now = datetime.datetime.now()
    age = now.year - bd
    print (("your intials are {}.{} and your age is {}".format(fn[0].upper(), ln[0].upper(), age)))


  #B = details("meytal", "avgil", 1980)

  ##print("the answer to the fifth excercise is:")
  ##print(B)




####sixth exercise - guess the number

import random
computer_number = (random.randint(1,10)) ### will select a number between 1 and 10
person_number = input("guess a number between 1 to 10:")

if person_number == computer_number:
    print ("the computer chose {}".format (computer_number))
    print ("you won!")
else:
    print("the computer chose {}".format(computer_number))
    print ("you lose")


if int(person_number) > int(computer_number):
    print ("the computer's number is smaller than your number")
elif person_number < computer_number:
    print ("the computer's number is bigger than your number")
else:
    print ("the computer's number is equal to your number")
