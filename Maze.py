# this is the one program to run in order to actually play the game

from __init__ import Hexamaze, Player1, Pos
from Guide import Guide
import Battle
import random
Hexamaze.make_maze()
end = Pos.make_end_goal()
Mazer = Guide(end)

print("Hello! Welcome to Hexamaze, the a-maze-ing game where you are lost.")
print("My name is Mazer and I will be lost with you.")
print("Now go and get us out of here before the monster eats us! Go! ")
print('\n')

while True:
    while True:
        move = raw_input("Pick a move: left, right, forward, or backward. ")
        while move not in Hexamaze.moves:
            move = raw_input("Make sure your move is either left, right, forward, or backward. ")
        new_pos = Player1.move_player(move)
        Pos.regulate()
        print Mazer.choose()
        if new_pos == end:
            print("You've reached the end! Yay! Oh no! What's that?")
            print("It's the monster! He wants to fight!")
            print('')
            if Battle.main():
                print("YOU WIN!!!")
                exit(420)
            else:
                print("Come on, man! The monster tossed you back into a random part of the maze...")
                xs = random.choice(range(6))
                ys = random.choice(range(6))
                Player1.position = [xs, ys]