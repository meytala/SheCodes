class calculator:
    def addition (x,y):
        added = x+y
        print (added)

    def subtraction (x,y):
        substract = x-y
        print(substract)

    def multification (x,y):
        multiply = x*y
        print (multiply)

    def devision (x,y):
        devide = x/y
        print(devide)


calculator.multification (3,5)
calculator.addition(4,5)


class human ():
    ###"this is a human class"
    def __init__ (self, human_gender = "unknown", age = 0, mood_level = "good", hunger_level = 0): ##the atributes
        self.human_gender = human_gender
        self.age = age
        self.mood_level = mood_level
        self.hunger_level = hunger_level

    def setGender (self): ##the functions (method)
        self.human_gender = input("please enter gender")

MrTsadok = human()  ##creat an object in the class human, named tsadok
MrTsadok.setGender()

print(MrTsadok.human_gender)


class cat():
    def __init__ (self, name, age, weight): ##the constructor - used to define the class
        self.name = name
        self.age = age
        self.weight = weight
        self.stomach = 0

    def feed (self, amount):
        self.stomach += amount

    def nextdate (self):
        self.weight = self.stomach +self.weight -0.25
        self.stomach = 0

    def speak (self):   ##the self refferes to a spesific object in the class, this object will change
        if self.stomach >0:
            return "prrrrr"
        else:
            return "meow!!!"

    def getName (self): ##the self is the object that the method is being called on
        return self.name

    def getWeight (self):
        return self.weight


cat1 = cat("mimi", 7, 20) ##cat 1 named mimi, her age is 7, and she weight 20
print (cat1.getName())


class Enemy:
    ##life = 3   ###this would be the difult variable  - will be the same for all objects
    def __init__(self, life):  ##instance variable, change based on the spesific object in the class
        self.life = life   ##the self life will have the value that you will give in the brakets

    def attack (self):
        print ("ouch")
        self.life -=1

    def check_enemy_life (self):
        if self.life <=0:
            print ("enemy is dead")
        else:
            print ("enemy life = " + str(self.life))

##to have anything inside a class, you need to access it.
##by creating an object

enemy_1 = Enemy(5)
enemy_1.attack()
enemy_1.check_enemy_life()


#######inheretence - take attribute and methods from a class that is already exist
class Human2:
    "this is a human class"
    def __init__ (self, human_gender = "human", age = 0):
        self.human_gender = human_gender
        self.age = age

    def speake (self):
        print ("i am a " + self.human_gender)

class Men(Human2): ##this is a child class that inherate the Human2 class
    "this is a man class"
    def __init__(self, haircolour, age):
        super().__init__(human_gender = "male", age = age)  ##super constructor - inherite all the constructors from the parent class, i,e, Human2
                                                            ## in this case, we overwrite the human_gender
                                                            ## and overwrite age over what we have in parent
        self.haircolour = haircolour


A_man = Men("brown", 50)
print ("the human is " + str(A_man.human_gender))
print ("the human age is " + str(A_man.age))
print ("te human haircolour is " + str(A_man.haircolour))
print(A_man.speake ())










