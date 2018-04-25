'''
Rock-Paper-Scissors game
Starter code for Stanford CME 193
author: Sven Schmit
'''

import agent

class Game:
    def __init__(self, agent1, agent2):
        self.moves_a1 = []
        self.moves_a2 = []
        self.nround = 0
        self.score_a1 = 0
        self.score_a2 = 0

        self.agent1 = agent1
        self.agent2 = agent2

        count_P = 0
        count_s = 0
        count_r = 0


    def round(self):
        print('Round {}: '.format(self.nround+1))
        # we pass along history so a player can take that into account when
        # deciding the next move
        move_a1 = self.agent1.getMove(self.moves_a2, self.moves_a1)
        move_a2 = self.agent2.getMove(self.moves_a1, self.moves_a2)


        # compare the moves and decide who wins

        outcome = self.compare(move_a1, move_a2)

        # output outcome of current round
        if outcome == 1:
            print('Player 1 wins: {} beats {}'.format(move_a1, move_a2))
            self.score_a1 +=1
        elif outcome == 0:
            print('This round is tied, both players played {}'.format(move_a1))
            self.score_a2 +=1
        else:
            print('Player 2 wins: {} beats {}'.format(move_a2, move_a1))

        # update scores

        print('scores: agent 1 score: {}; agent 2 score: {}'.format(self.score_a1, self.score_a2))


        self.moves_a1.append(move_a1)
        self.moves_a2.append(move_a2)



    def play(self, nrounds):
        for r in range(nrounds):
            self.round()
            self.nround += 1

    def summary(self):
        # print some summary of the games
        print('='*20)
        if self.score_a1 > self.score_a2:
            print('Player 1 wins')
        elif self.score_a1 < self.score_a2:
            print('Player 2 wins')
        else:
            print('The game ends in a tie')

        print('Final score: {} - {}'.format(self.score_a1, self.score_a2))

        # To implement: find the move that was played most often

        def count_moves ():
            number_of_p = 0
            number_of_s = 0
            number_of_r = 0

            for i in self.moves_a1:
                if i == "p":
                    number_of_p +=1
                elif i == "s":
                    number_of_s +=1
                else:
                    number_of_r +=1

            for i in self.moves_a2:
                if i == "p":
                    number_of_p +=1
                elif i == "s":
                    number_of_s +=1
                else:
                    number_of_r +=1

            print ("p was played in the game {} times".format (number_of_p))
            print ("s was played in the game {} times".format (number_of_s))
            print ("r was played in the game {} times".format (number_of_r))

            dict_of_prs = {"p":number_of_p, "r":number_of_r, "s":number_of_s}
            most_freq = max(dict_of_prs, key=dict_of_prs.get)

            print('Most played move: {}'.format(most_freq))
            print('='*20)

    def compare(self, move_a1, move_a2):
        if move_a1 == move_a2:
            return 0
        elif (move_a1=="r" and move_a2=="p" or
              move_a1=="p" and move_a2=="s" or
              move_a1=="s" and move_a2=="r"):
            return 2
        else:
            return 1





human = agent.HumanAgent()
Computer = agent.InstructorAgent()

game = Game(human, Computer)

game.play(5)
game.summary()






