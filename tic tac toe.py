import random
def winner(a,b,c):
    if((a == b)&(b==c)):
        return True

players_decided=False

while players_decided == False:
    player1 = input("player 1 would you like to be X or O ").upper()
    if player1 == "X":
        print("player 2 you are O")
        player2 = "O"
        players_decided = True
    elif player1 == "O":
        print("player 2 you are X")
        player2 = "X"
        players_decided = True
    else:
        print("Player 1 pick X or O")


a1 = " "
a2 = " "
a3 = " "

b1 = " "
b2 = " "
b3 = " "

c1 = " "
c2 = " "
c3 = " "

turn = random.randint(1,2)

on = True

print(f" 1  2  3 \nA {a1}|{a2}|{a3} \n--------- \nB {b1}|{b2}|{b3}\n---------  \nC {c1}|{c2}|{c3}\n")

while(on):
    if(turn == 1 ):
        move = input("Player 1 make a move ").lower()
        if(move == "a1"):
            if (a1 == "X") | (a1 == "O"):
                print("This spot is taken already")
            else:
                a1 = player1
                print(f" 1  2  3 \nA {a1}|{a2}|{a3} \n--------- \nB {b1}|{b2}|{b3}\n---------  \nC {c1}|{c2}|{c3}\n")
                turn = 2
        elif (move == "a2"):
            if (a2 == "X") | (a2 == "O"):
                print("This spot is taken already")
            else:
                a2 = player1
                print(f" 1  2  3 \nA {a1}|{a2}|{a3} \n--------- \nB {b1}|{b2}|{b3}\n---------  \nC {c1}|{c2}|{c3}\n")
                turn = 2
        elif (move == "a3"):
            if (a3 == "X") | (a3 == "O"):
                print("This spot is taken already")
            else:
                a3 = player1
                print(f" 1  2  3 \nA {a1}|{a2}|{a3} \n--------- \nB {b1}|{b2}|{b3}\n---------  \nC {c1}|{c2}|{c3}\n")
                turn = 2
        elif (move == "b1"):
            if (b1 == "X") | (b1 == "O"):
                print("This spot is taken already")
            else:
                b1 = player1
                print(f" 1  2  3 \nA {a1}|{a2}|{a3} \n--------- \nB {b1}|{b2}|{b3}\n---------  \nC {c1}|{c2}|{c3}\n")
                turn = 2
        elif (move == "b2"):
            if (b2 == "X") | (b2 == "O"):
                print("This spot is taken already")
            else:
                b2 = player1
                print(f" 1  2  3 \nA {a1}|{a2}|{a3} \n--------- \nB {b1}|{b2}|{b3}\n---------  \nC {c1}|{c2}|{c3}\n")
                turn = 2
        elif (move == "b3"):
            if (b3 == "X") | (b3 == "O"):
                print("This spot is taken already")
            else:
                b3 = player1
                print(f" 1  2  3 \nA {a1}|{a2}|{a3} \n--------- \nB {b1}|{b2}|{b3}\n---------  \nC {c1}|{c2}|{c3}\n")
                turn = 2
        elif (move == "c1"):
            if (c1 == "X") | (c1 == "O"):
                print("This spot is taken already")
            else:
                c1 = player1
                print(f" 1  2  3 \nA {a1}|{a2}|{a3} \n--------- \nB {b1}|{b2}|{b3}\n---------  \nC {c1}|{c2}|{c3}\n")
                turn = 2
        elif (move == "c2"):
            if (c2 == "X") | (c2 == "O"):
                print("This spot is taken already")
            else:
                c2 = player1
                print(f" 1  2  3 \nA {a1}|{a2}|{a3} \n--------- \nB {b1}|{b2}|{b3}\n---------  \nC {c1}|{c2}|{c3}\n")
                turn = 2
        elif (move == "c3"):
            if (c3 == "X") | (c3 == "O"):
                print("This spot is taken already")
            else:
                c3 = player1
                print(f" 1  2  3 \nA {a1}|{a2}|{a3} \n--------- \nB {b1}|{b2}|{b3}\n---------  \nC {c1}|{c2}|{c3}\n")
                turn = 2

    elif(turn == 2 ):
        move = input("Player 2 make a move ").lower()
        if(move == "a1"):
            if (a1 == "X") | (a1 == "O"):
                print("This spot is taken already")
            else:
                a1 = player2
                print(f" 1  2  3 \nA {a1}|{a2}|{a3} \n--------- \nB {b1}|{b2}|{b3}\n---------  \nC {c1}|{c2}|{c3}\n")
                turn = 1
        elif (move == "a2"):
            if (a2 == "X") | (a2 == "O"):
                print("This spot is taken already")
            else:
                a2 = player2
                print(f" 1  2  3 \nA {a1}|{a2}|{a3} \n--------- \nB {b1}|{b2}|{b3}\n---------  \nC {c1}|{c2}|{c3}\n")
                turn = 1
        elif (move == "a3"):
            if (a3 == "X") | (a3 == "O"):
                print("This spot is taken already")
            else:
                a3 = player2
                print(f" 1  2  3 \nA {a1}|{a2}|{a3} \n--------- \nB {b1}|{b2}|{b3}\n---------  \nC {c1}|{c2}|{c3}\n")
                turn = 1
        elif (move == "b1"):
            if (b1 == "X") | (b1 == "O"):
                print("This spot is taken already")
            else:
                b1 = player2
                print(f" 1  2  3 \nA {a1}|{a2}|{a3} \n--------- \nB {b1}|{b2}|{b3}\n---------  \nC {c1}|{c2}|{c3}\n")
                turn = 1
        elif (move == "b2"):
            if (b2 == "X") | (b2 == "O"):
                print("This spot is taken already")
            else:
                b2 = player2
                print(f" 1  2  3 \nA {a1}|{a2}|{a3} \n--------- \nB {b1}|{b2}|{b3}\n---------  \nC {c1}|{c2}|{c3}\n")
                turn = 1
        elif (move == "b3"):
            if (b3 == "X") | (b3 == "O"):
                print("This spot is taken already")
            else:
                b3 = player2
                print(f" 1  2  3 \nA {a1}|{a2}|{a3} \n--------- \nB {b1}|{b2}|{b3}\n---------  \nC {c1}|{c2}|{c3}\n")
                turn = 1
        elif (move == "c1"):
            if (c1 == "X") | (c1 == "O"):
                print("This spot is taken already")
            else:
                c1 = player2
                print(f" 1  2  3 \nA {a1}|{a2}|{a3} \n--------- \nB {b1}|{b2}|{b3}\n---------  \nC {c1}|{c2}|{c3}\n")
                turn = 1
        elif (move == "c2"):
            if (c2 == "X") | (c2 == "O"):
                print("This spot is taken already")
            else:
                c2 = player2
                print(f" 1  2  3 \nA {a1}|{a2}|{a3} \n--------- \nB {b1}|{b2}|{b3}\n---------  \nC {c1}|{c2}|{c3}\n")
                turn = 1
        elif (move == "c3"):
            if (c3 == "X") | (c3 == "O"):
                print("This spot is taken already")
            else:
                c3 = player2
                print(f" 1  2  3 \nA {a1}|{a2}|{a3} \n--------- \nB {b1}|{b2}|{b3}\n---------  \nC {c1}|{c2}|{c3}\n")
                turn = 1

    if winner(a1,a2,a3):
        if(player1 == a1):
            print("Player 1 you're the winner!!!")
            on = False
        elif(player2 == a1):
            print("Player 2 you're the winner!!!")
            on = False
    elif winner(b1,b2,b3):
        if(player1 == b1):
            print("Player 1 you're the winner!!!")
            on = False
        elif(player2 == b1):
            print("Player 2 you're the winner!!!")
            on = False
    elif winner(c1,c2,c3):
        if(player1 == c1):
            print("Player 1 you're the winner!!!")
            on = False
        elif(player2 == c1):
            print("Player 2 you're the winner!!!")
            on = False
    elif winner(a1,b1,c1):
        if(player1 == a1):
            print("Player 1 you're the winner!!!")
            on = False
        elif(player2 == a1):
            print("Player 2 you're the winner!!!")
            on = False
    elif winner(a2,b2,c2):
        if(player1 == a2):
            print("Player 1 you're the winner!!!")
            on = False
        elif(player2 == a2):
            print("Player 2 you're the winner!!!")
            on = False
    elif winner(a3,b3,c3):
        if(player1 == a3):
            print("Player 1 you're the winner!!!")
            on = False
        elif(player2 == a3):
            print("Player 2 you're the winner!!!")
            on = False
    elif winner(a1,b2,c3):
        if(player1 == a1):
            print("Player 1 you're the winner!!!")
            on = False
        elif(player2 == a1):
            print("Player 2 you're the winner!!!")
            on = False
    elif winner(c1,b2,a3):
        if(player1 == c1):
            print("Player 1 you're the winner!!!")
            on = False
        elif(player2 == c1):
            print("Player 2 you're the winner!!!")
            on = False