movie = ["the notebook", "maleficent", "butmen v supermen",
         "black swan", "gone girl", "war of the worlds", "just_married"]

actors = ["Rachel Mcadams", "Angelina july", "Gal gadot",
          "Natalie portman", "rosamund pike","britney murphy"]

# my_list = []
# for (i, s) in enumerate(["a", "b", "c"]):
#     my_list.append(i*s)
# my_list2 = [i*s for (i,s) in enumerate(["a", "b", "c"])]

print("targil 1:")

yosi = zip(movie, actors)
targil_1 = [k+" is played by "+v for (k,v) in yosi]
print(targil_1)

print("targil 2:")

movies = dict(zip(movie, actors))
print(movies)


print ("targil 3:")

targil_3=[k+" is played by "+v for (k,v) in movies.items()]
print(targil_3)

print ("targil 4:")
#צרו רשימת הכפלה ב- 100 של כל מספר מ -1 עד 9 (כולל) אם הןא מתחלק ב 2 ללא שארית
#[200, 400, 600, 800]

targil4 = [i*100 for i in range(1,10) if i%2==0]
print(targil4)

print ("targil 5:")
# #צרו רשימת הכפלה ב- 100 של כל מספר מ -1 עד 9 (כולל) אם הןא מתחלק ב 2 ללא שארית.
# #אם יש שארית השאירו את המספר בלי להכפיל ב100
# #[1,200,3,400,5,600,7,800,9]
#
targil5 = [(i*100 if i%2==0 else i) for i in range (1,10) ]
print(targil5)

print ("targil 6:")
#יצרו רשימה של 7 בום

targil6 = ["boom" if i%7==0 else i for i in range (1,100) ]
print(targil6)

print("targil 7:")
add = lambda x, y : x + y
print(add(1,2))

print("targil 8:")
joules = [5000, 8000, 1000, 12000]
#4184
new_list = [print(i, n) for (i,n) in zip(joules, map(lambda i: i/4184,joules))]

print("targil 9:")
combinations = [print(i,n) for (i) in range(1,7) for n in range(1,7)]

print("targil 10:")
languages = ["htmal", "java", "python", "ruby"]
my_language = list(filter(lambda a: a=="python", languages))
print (my_language)


##------------------------------------------------------------
print("FIRST exc")

def revert (s,t):
    revers_t = ""
    for i in range(len(t)):
        revers_t = revers_t +t[-i-1]
    if revers_t == s:
       print ("t is revert of s")
    else:
       print ("t is not revert of s")

print(revert("cat", "rat"))


print("SECOND exc")
def romi(x):
    translate = 0
    for i in range(0,len(x)):
        if x[i] == "I":
            translate += 1
        elif x[i] == "V":
            translate +=5
        elif x[i] == "X":
            translate +=10
        else:
            translate +=50
    print(translate)

print(romi("XVII"))


print("THIRD exc")

def plus_1(a):
    new_number = ''.join(str(e) for e in a)  ##conver the element of a and join them, a is str
    new_number_as_int = int(new_number)      ##convert a (str), to integer
    new_number_plus = new_number_as_int + 1  ##add 1 to the integer
    new_string = str(new_number_plus)        ## convert the new number to a string
    answer = []                              ## create a new list
    for i in new_string:
        answer.append(i)
    print(answer)

digit=[4,3]
plus_1(digit)


print ("FORTH exc")

import random
import string


def cows_and_bulls (a):
    Bools = 0
    while Bools <5:
        guess_a_word = input("Guess a random word with 5 upper case: ").upper()
        Hit = 0
        Bools = 0
        print ("random word is: ", a)
        print ("your word is: ", guess_a_word)
        for i in range(len(a)):
            if guess_a_word[i].isdigit()==True:
                print ("print only letters (no numbers alowed)")
                break
            elif len(guess_a_word)>5 or len(guess_a_word)<5 :
                print ("your word should be 5 letters length")
                break
            elif  guess_a_word[i]== a[i]:
                Bools +=1
            elif  a[i] in guess_a_word:
                  Hit +=1
        print ("Hit =",Hit, "Bools =",Bools)
    print("you win!")

random_string = ''.join([random.choice(string.ascii_uppercase) for n in range(5)])
print(random_string)

cows_and_bulls (random_string)
