###the while loop will continue to execute as long as the condition is true.
# In other words, instead of executing if something is true it executes while that thing is true.

def picture (n):
    for i in range (0,n+1):
        print (i*"*")
        i +=1
picture (4)

print ('first option for trapez:')
def picture (n):
    for i in range (0,n+1):
        print (i*"*"+4*'*')
        i +=1
picture (4)

print ('second option for trapez:')
def picture (n):
    while n < 9:
        print (n*"*")
        n+=1
picture (4)


print ('meuyan:')
i =0
while i<4:
    print (i*"*")
    i+=1
i=2
while i >0:
    print (i*"*")
    i -=1



###targil 2

#print ('guess number:')

#import random
#computer_number = (random.randint(1,10)) ### will select a number between 1 and 10
##person_number = input("guess a number between 1 to 10:")


# def guess_a_number():
#     num_guess = 0
#     ##print(computer_number)
#     while num_guess <3:
#         n=input("guess a number between 1 to 10:")
#         if int(n)==computer_number:
#             print ("the computer chose {}, you won!".format (computer_number))
#             break
#         if int(n) > int(computer_number):
#             print ("the computer's number is smaller than your number, try again")
#         else:
#             print ("the computer's number is bigger than your number, try again")
#         num_guess +=1
#     else: print ("GAME OVER")


# guess_a_number ()


####7 boom
# print ("7 boom")




def seven_boom1 (turn):
     if turn%7 == 0:
         print ("the COMPUTER guessed:")
         print ("boom")
         print ("whats YOUR next number?")
     else:
         print ("the COMPUTER guessed:")
         print (turn)
         print ("whats YOUR next number?")

#seven_boom1()


def seven_boom2(turn):
    answer = input("next number:")
    if turn%7 != 0:
        while int(answer) == turn:
            print ("what's the COMPUTER'S next number?")
            return False
        else:
            print ("Wrong")
            return True
    else:
        while answer == "boom":
              print ("what's the COMPUTER'S the next number?")
              return False
        else:
            print ("Wrong")
            return True

#seven_boom2 ()


def play ():
    print ("start play:")
    for turn in range (1,50):
        if turn%2!=0:
            seven_boom1(turn)
        else:
            Game_over = seven_boom2(turn)
            if Game_over == True:
               print ("GAME OVER")
               return


play()




