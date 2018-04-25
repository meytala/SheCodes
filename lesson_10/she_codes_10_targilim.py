print ("Exercise 2:")

#Rewrite the Person class so that a person’s age is calculated for the first time when a new person instance is created,
#  and recalculated (when it is requested) if the day has changed since the last time that it was calculated.

import datetime # we will use this for date objects

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email
        self.calculate_age()
        #self.re_calculate_age()

    def calculate_age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        self.age = age

person = Person(
    "Jane",
    "Doe",
    datetime.date(1992, 3, 12), # year, month, day
    "No. 12 Short Street, Greenville",
    "555 456 0987",
    "jane.doe@example.com"
)

print(person.name)
print(person.email)
print(person.age)



class Smith:
    surname = "Smith"
    profession = "smith"

    def __init__(self, name, profession=None):
        self.name = name
        if profession is not None:
            self.profession = profession

meytal = Smith("meytal", "epi")
print(meytal.profession)



# print("targil 4")
#
# class Artist:
#     def __init__ (self, artist_name):
#         self.artist_name = artist_name
#
# class Song:
#     def __init__ (self, song_name, album, artist_name, year):
#         self.songe_name = song_name
#         self.album = album
#         self.artist_name = Artist(artist_name)
#         self.year = year
#
# Class Play_list:
#     def __init__ (self, play_list_name, songs):
#         self.play_list_name = play_list_name
#         self.songs = songs
#
#
# class Album:
#     def __init__ (self, album_name, artist_name, songs, )


print ("targil 5")
from math import gcd

class Rational:
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def print_rational (self):
        answer = self.p/self.q
        return("the answer is {}".format (answer))

    def GCD (self):
        minimal_common = (gcd(self.p, self.q))
        new_p=self.p/minimal_common
        new_q=self.q/minimal_common
        return("the GCD is {}/{}".format(int(new_p),int(new_q)))

    def adding(self):
#        total = self.p + self.q
        total = self.p.__add__(self.q)
        return(total)

    def substruct (self):
#        sunstruction = self.p - self.q
        sunstruction = self.p.__sub__(self.q)
        return (sunstruction)

    def multiply (self):
        multp = self.p.__mul__(self.q)
        return (multp)

    def divid (self):
        divide = self.p.__truediv__(self.q)
        return (divide)

    def equal (self):
        if self.p == self.q:
            return ("The numbers are equal")
        else:
            return ("The numbers are not equal")

    def float(self):
        p=self.p.__float__()
        q=self.q.__float__()
        return ("the floating numbers are {} and {}".format (p,q))

half = Rational (8,20)
print (half.print_rational())
print (half.GCD())
print (half.adding())
print (half.substruct())
print (half.multiply())
print (half.divid())
print (half.equal())
print (half.float())


print ("targil 6:")

class TreeNode:
    def __init__(self, value, right = None, left = None):
        self.right = right
        self.left = left

    def print_tree (self):
        print (self.value)
        print (self.right)
        print (self.left)


    def new_right (self, value_right):
        self.right = value_right

    def looks_up (self, value_to_search):
        if value_to_search == self.right:
            print ("your value is on the right branch")
        elif value_to_search == self.left:
            print ("your value is on the left branch")
        else:
            print ("Your value is not in the tree")

     def remove_value (self, value_to_remove):
        if value_to_remove == self.right:
            self.right = Null
        elif value_to_remove == self.left:
            self.left = Null
        else:
            print ("the value is not in the tree")

