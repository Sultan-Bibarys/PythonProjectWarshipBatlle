from random import randint
import random
from ggg import ggg



#from datetime import date
##########################3

class T:
    def __init__(a,):
        import time
        a.TIME=time.strftime('%H:%M:%S')
a=T()
B=a.TIME
print(B)
###############################################
print('SEA BATTLE on field 5x5')
print('Do you want to play a game?')
print('Y---YES             N---NO')
reply = input('Your reply: ')
if reply== 'y' or reply == "Y":
    ggg1=ggg()
    ggg2=ggg()


    name=str(input('what is your name:'))
    age=int(input('How  old are you?:'))
    ggg1.set_name(name)
    ggg1.set_age(age)

    ggg1.description_of_person()
 ###########################################   
    name=input('Your name?: ')
    surname=input('Your surname? ')
    ns=str(name)+' '+str(surname)
    with open('Players.txt','a') as p:
        p.write(ns)
           
            
        
    def field():
        board=[]
        print ("let's play Battleship")
        for x in range (5):       #############
            board.append(['0']*5)
        def print_board(board):
            for row in board:
                print ((' ').join(row))
                
        print_board(board)
##################SHIFTSHIFT######################################
        def random_row(board):
            return randint(0,len(board)-1)
        def random_col(board):
            return randint(0,len(board[0])-1)
        ship_row=random_row(board)
        ship_col=random_col(board)
#####################################################
        print (ship_row)
        print (ship_col)
#####################################3
        b=T()
        q=b.TIME
        print(q)

        def awer():
            print('DO YOU WANT PLAY AGAIN?')
            print('Y--------YES           N-------NO')
            answer = input('Your answer?: ')
            if answer =='y' or answer  == 'Y':
                lool=T()
                Bq=lool.TIME
                print(Bq)
                field()
            else:
                print('GOOD BYE')
                exit()
                
###############33############3###############333
        def game():
            k = 0
            while k <15:
                def player():
                    
                    print('WALK',name)
                    guess_row,guess_col=map(int,input('gues row and column(write without space): '))
                  
                    if ship_row==guess_row and ship_col==guess_col:
                        print('!!!!!YOU WIN!!!!!!')
                        ll=T()
                        ol=ll.TIME
                        print(ol)
                        board[guess_row][guess_col]= 'x'
                        print_board(board)
                        awer()
                        
                        
                    else:
                        board[guess_row][guess_col]= '*'
                        print_board(board)
                    
                    
                player()       
#######################################################################################
                def ranplay():
                  
                    print('WALK enemy')
                    with open('random player.txt','r') as p:
                        for line in p:
                            line = line[0:-1].split(' ')
                    walk =random.choice(line)
                    ran_row,ran_col=map(int,walk)
                            
                    board[ran_row][ran_col]= '*'
                    print_board(board)
                    
                    if ship_row==ran_row and ship_col==ran_col:
                        print('YOU LOSE ')
                        uoy=T()
                        Be=uoy.TIME
                        print(Be)
                        board[ran_row][ran_col]= ''
                        print_board(board)
                        awer()
                        
                ranplay()       
            k+=1
           
            
        game()
           
###########################################################################3333333
#############################################################################3
           
    field()
    
            
            
                                                
                                          
                                           
                               
                      






