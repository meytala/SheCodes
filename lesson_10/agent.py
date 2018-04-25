'''
Rock-Paper-Scissors game
Starter code for Stanford CME 193
author: Sven Schmit
'''

import random

class Agent:
    def getMove(self, moves_other, moves_self):
        pass


class InstructorAgent(Agent):
    def __init__(self):
        p_rock = random.random()
        p_scissors = random.random()
        p_paper = random.random()
        p_total = p_rock + p_scissors + p_paper

        self.p_rock = p_rock / p_total
        self.p_scissors = self.p_rock + p_scissors / p_total

    def getMove(self, moves_other, moves_self):
        random_move = random.random()
        if random_move < self.p_rock:
            move = 'r'
        elif random_move < self.p_scissors:
            move = 's'
        else:
            move = 'p'
        print ("computer move is {}".format (move))
        return move


class HumanAgent(Agent):
    def getMove(self, moves_other, moves_self):
        user_input = ""
        while user_input not in ("p","s","r"):
            user_input = input("What's your move? write S for scissors, P for Paper or R for Rock").lower()
            if user_input in ("p","s","r"):
                print ("your choise is {}".format (user_input))
                return user_input
            else:
                print ("you can only choose p, s, or r")



# class MyAgent(Agent):
#     def getMove(self, moves_a1, moves_a2):
#
#         # YOUR CODE HERE
#
#         pass




# a1 = Agent
# a2 = Agent
#
# human = HumanAgent(a1)
# Computer = InstructorAgent(a2)
