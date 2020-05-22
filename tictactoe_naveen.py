import random  # import random




def display(board):  # display the board
    print("\n" * 100)  # refresh the board
    print("{}|{}|{}".format(board[0], board[1], board[2]))
    print("{}|{}|{}".format(board[3], board[4], board[5]))
    print("{}|{}|{}".format(board[6], board[7], board[8]))







def decide_first():  # decide who start first
    player = random.randint(1, 2)
    return player


def choose_marker(p1_name,p2_name): #let players choose their preferred marker
    first = decide_first()
    choice =' '
    while(choice !='O' or choice!= 'X'):
        if (first == 2):
            choice = input("{} goes first. Choose O or X ".format(p2_name)).upper()
            if choice == 'O':
                return ('X','O',first)
            else:
                return ('O', 'X',first)
        else:
            choice = input("{} goes first. Choose O or X ".format(p1_name)).upper()
            if choice == 'X':
                return ('X','O',first)
            else:
                return ('O', 'X',first)


def place_marker(board,marker,position,):
    position = position - 1
    board[position] = marker


def win_win(board,mark):
    return (                #horizontal wins
            (board[0] == mark and board[1] == mark and board[2] == mark) or
            (board[3] == mark and board[4] == mark and board[5] == mark) or
            (board[6] == mark and board[7] == mark and board[8] == mark) or
                            #vertical wins
            (board[0] == mark and board[3] == mark and board[6] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
                            #diangonal wins
            (board[0] == mark and board[4] == mark and board[8] == mark) or
            (board[2] == mark and board[4] == mark and board[6] == mark) )




def check_empty(board,pos):
    pos = pos -1
    return (board[pos] != 'X' and board[pos] != 'O')

def board_full(board):
    for i in range(0,9):
        if(check_empty(board,i)):
            return False #board not full
    return True #board full

def play_again():
    return input(("Do you wanna play again: ").lower().startswith('y'))


def player_choice(board,name):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not check_empty(board, position):
        position = int(input(("{} choose your next position: (1-9) ").format(name)))

    return position

replay = True
while replay:
    print("\n"*100)
    print('Welcome to Tic Tac Toe!')
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    p1_name = input("Enter player 1 name: ")
    p2_name = input("Enter player 2 name: ")
    turn = 0
    p1_marker,p2_marker,turn = choose_marker(p1_name,p2_name)

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        input("Press any key to exit.......")
        break
    while game_on:
        if turn == 1 :
            display(board)
            pos = player_choice(board,p1_name)
            place_marker(board,p1_marker,pos)

            if win_win(board,p1_marker):
                display(board)
                input("Congratulations {} has won!\n Press enter to continue... ".format(p1_name))
                break
            elif board_full(board) :
                display(board)
                input("Its a draw!\n Press enter to continue... ")
                break
            else:
                turn = turn + 1
        else:
            if turn ==2 :
                display(board)
                pos = player_choice(board, p2_name)
                place_marker(board, p2_marker, pos)

                if win_win(board, p2_marker):
                    display(board)
                    input("Congratulations {} has won!\n Press enter to continue... ".format(p2_name))
                    break
                elif board_full(board):
                    display(board)
                    input("Its a draw!\n Press enter to continue... ")
                    break
                else:
                    turn = turn - 1

    print("Test")
    replay= input("Do you wanna play again : Y/N ").upper()
    if(replay[0] == 'n' ):
        input("Thank you for playing!!!!\nPress any key to exit.....")
        break









    


