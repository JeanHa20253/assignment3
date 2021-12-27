from replit import clear
import os

def position_index():
    clear()
    print('     1     |      2      |      3    ')
    print('--------------------------------------')
    print('     4     |      5      |      6    ')
    print('--------------------------------------')
    print('     7     |      8      |      9    ')


_='--------------------------------------'

A1='    '
A2='    '
A3='    '
B1='    '
B2='    '
B3='    '
C1='    '
C2='    '
C3='    '
equal_space='    '

position=[1,2,3,4,5,6,7,8,9]
win_index=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
sepa='|'
playerA='X'
playerB='O'
all_cells = [A1, A2, A3, B1, B2, B3, C1, C2, C3]
game=True

scoreA=0
scoreB=0

def update_move():
    global all_cells
    rowA_t= ''.join([cell+equal_space+sepa for cell in all_cells[:3]])
    rowB_t=''.join([cell+equal_space+sepa for cell in all_cells[3:6]])
    rowC_t=''.join([cell+equal_space+sepa for cell in all_cells[-3:]])
    the_game= f'{rowA_t}\n{_}\n{rowB_t}\n{_}\n{rowC_t}\n'
    return the_game


def lose_win(player):
    global all_cells, win_index, game
    for win in win_index:
        if player in all_cells[win[0]] and player in all_cells[win[1]] and player in all_cells[win[2]]:
            print(f'{player} wins')
            game = False
            return player

    for cell in all_cells:
        if playerA in cell or playerB in cell:
            print(f'It is a draw')
            game=False
            return 'Draw'



def update_score(player):
    global scoreA, scoreB
    if player==playerA:
        scoreA+=1
    if player==playerB:
        scoreB+=1
    if player=="Draw":
        return



def go_first(player):
    if player== playerA:
        Aposition = int(input('What is your move, player A?'))
        all_cells[position.index(Aposition)] += playerA
        print(update_move())
        lose_win(playerA)
        if game==False:
            return

        Bposition = int(input('What is your move, player B?'))
        all_cells[position.index(Bposition)] += playerB
        print(update_move())
        lose_win(playerB)
        if game==False:
            return
    elif player== playerB:
        Bposition = int(input('What is your move, player B?'))
        all_cells[position.index(Bposition)] += playerB
        print(update_move())
        lose_win(playerB)
        if game == False:
            return
        Aposition = int(input('What is your move, player A?'))
        all_cells[position.index(Aposition)] += playerA
        print(update_move())
        lose_win(playerA)
        if game==False:
            return



next_round= True



while next_round:
    position_index()
    #
    # Aposition= int(input('What is your move, player A?'))
    # all_cells[position.index(Aposition)] += playerA
    # print(update_move())
    # lose_win(playerA)
    #
    #
    # Bposition= int(input('What is your move, player B?'))
    # all_cells[position.index(Bposition)] += playerB
    # print(update_move())
    # lose_win(playerB)















