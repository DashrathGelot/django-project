from IPython.display import clear_output
import random
def displayboard(board):
    clear_output()
    print(' ',board[7],'|',board[8],'|',board[9])
    print('------------')
    print(' ',board[4],'|',board[5],'|',board[6])
    print('------------')
    print(' ',board[1],'|',board[2],'|',board[3])

def sign():
    '''OUTPUT=(player 1 marker,player 2 marker)'''
    mark=''
    while mark!='X' and mark!='O':
        mark=input('player 1 choose X or O : ').upper()
    if mark=='X':
        return ('X','O')
    else:
        return ('O','X')

def position(board,mark,player):
    pos=int(input(f'enter {player} your position '))
    if board[pos]!='':
        print('this position is allready fill up ')
        position(board,mark,player)
    else:
        board[pos]=mark
  

def win(board,mark):
    return ((board[1]==mark and board[2]==mark and board[3]==mark) or
    (board[4]==mark and board[5]==mark and board[6]==mark) or
    (board[7]==mark and board[8]==mark and board[9]==mark) or
    (board[1]==mark and board[4]==mark and board[7]==mark) or
    (board[2]==mark and board[5]==mark and board[8]==mark) or
    (board[3]==mark and board[6]==mark and board[9]==mark) or
    (board[1]==mark and board[5]==mark and board[9]==mark) or
    (board[7]==mark and board[5]==mark and board[3]==mark))


def choose_first():
    if random.randint(0,1)==0:
        return 'player1'
    else:
        return 'player2'

def board_full(board):
    for i in range(1,10):
        if board[i]=='':
            return False
    return True

def replay():
    return input('do you want a play again (y/n)').startswith('y')


print("hello Welcome to tic tac toe ")

while True:
    board=['']*10
    player1_marker,player2_marker=sign()
    turn=choose_first()
    print(turn+' will go first')
    ans=input('are you ready for play (y/n)')
    if ans=='y':
        game=True
    else:
        game=False
    while game: 
        if turn=='player1':
            displayboard(board)
            position(board,player1_marker,'player1')
            if win(board,player1_marker):
                displayboard(board)
                print('congratulations ! you have won the match')
                game=False
                
            else:
                if board_full(board):
                    displayboard(board)
                    print('match is draw')
                    game=False
                else:
                    turn='player2'
        else:
            displayboard(board)
            position(board,player2_marker,'player2')
            if win(board,player2_marker):
                displayboard(board)
                print('congratulations ! you have won the match')
                game=False
                
            else:
                if board_full(board):
                    displayboard(board)
                    print('match is draw')
                    game=False
                else:
                    turn='player1'
    if not replay():
        break