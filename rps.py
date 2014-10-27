import time
from random import randint
wins,losses  = 0, 0

def rps_song():
        print "Rock..."
        time.sleep(0.5)
        print "Paper..."
        time.sleep(0.5)
        print "Scissor...!"
        time.sleep(1) 

def game(wins, losses):
        print "Rock, Paper or Scissors?"
        user_choice = raw_input()
        while(user_choice != ("Rock" or "Paper" or "Scissors")):
                print "Error, select a proper option(Case Sensitive):"
                user_choice = raw_input()
        rps_song()
        comp_choice = randint(0,2)
        
        if user_choice == "Rock":
                if comp_choice == 0:
                        print "Its a draw"
                        end(wins, losses)
                elif comp_choice == 1:
                        print "Paper beats Rock you lost"
                        losses += 1
                        end(wins, losses)
                elif comp_choice == 2:
                        print "Rock beats Scissors you won"
                        wins += 1
                        end(wins, losses)
        
        if user_choice == "Paper":
                if comp_choice == 0:
                        print "Paper beats Rock you won"
                        wins += 1
                        end(wins, losses)
                elif comp_choice == 1:
                        print "Its a draw"
                        end(wins, losses)
                elif comp_choice == 2:
                        print "Scissors beats Paper you lost"
                        losses += 1
                        end(wins, losses)
 
        if user_choice == "Scissors":
                if comp_choice == 0:
                        print "Rock beats Scissors you lost"
                        losses += 1
                        end(wins, losses)
                elif comp_choice == 1:
                        print "Scissors beats Paper you won"
                        wins += 1
                        end(wins, losses)
                elif comp_choice == 2:
                        print "Its a draw"
                        end(wins, losses)
        
def end(wins, losses):
        print "Wins: " + str(wins) + " losses: " + str(losses)
        print "Do you want to play again?"
        user_input = raw_input()
        if user_input == "Yes":
                game(wins, losses)
 
print "Want to play Rock Paper Scissors?('Yes' to play, type anything else to quit)"
user_input = raw_input()
if user_input == "Yes":
        game(wins, losses)