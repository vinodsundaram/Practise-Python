# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 21:05:16 2016

@author: Vinod
Game : Rock Papper Scissor game
"""
import os
clear = lambda: os.system('cls')
clear()

print("** Rock Papper Scissor - 2 player game **")
p1=input("Player 1, Enter your name:")
p2=input("Player 2, Enter your name:")
quit=""
while quit!='enter':
    clear()    
    print("** Instructions **")
    #print("Ökay %s and %s" %p1 %p2)    
    print("** Enter r-rock p-paper s-scissor **")
    player1=input("Your move, "+p1+" : ")
    player2=input("Your move, "+p2+" : ")
    
    if (player1 == "r" and player2=="s") or (player1 == "s" and player2=="p") or (player1 == "p" and player2=="r"):
        print("Player1 wins")
    elif (player2 == "r" and player1=="s") or (player2 == "s" and player1=="p") or (player2 == "p" and player1=="r"):
        print("Player2 wins")
    else:
        print("Ohh no!! Equally competent, Match Draw")
    
    quit=input("Type 'enter' to quit: ")

    