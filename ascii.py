import time 
from colorama import Fore 
import sys 
import random
title='tic tac toe'
x='x'.upper()
o='o'.upper()
colors=(Fore.RED,Fore.GREEN,Fore.BLUE,Fore.YELLOW)
def error_msg(txt=''):
    for text in txt:
        sys.stderr.flush()
        time.sleep(0.1)
        sys.stderr.write(f'{colors[0]}{text}')
    else:
        global reset_to_default_color 
        reset_to_default_color=Fore.RESET 
        print(f'{reset_to_default_color}')
        
error_msg()
for txt in title:
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write(f'\t{random.choice(colors)}{txt.upper()}')
else:
    print(f'{reset_to_default_color}')
    time.sleep(0.2)
    print('Creating the board....\n')
    time.sleep(0.2)
    def create_board():
        global game_board
        global join_game_board
        game_board=['-','-','-','\n-','-','-','\n-','-','-']
        join_game_board=" ".join(game_board)
        print(f'{join_game_board}')
        
    create_board()
                
    def win_condition(player_1_symbol,player_2_symbol):
        player_1_won_msg='PLayer 1 won!'
        player_2_won_msg='Player 2 won!'
        tie_msg='Its a tie, nobody wins' 
        if game_board[0]==player_1_symbol and game_board[1]==player_1_symbol and game_board[2]==player_1_symbol:
            sys.exit(f'{player_1_won_msg}')
        elif game_board[0]==player_2_symbol and game_board[1]==player_2_symbol and game_board[2]==player_2_symbol:
            sys.exit(f'{player_2_won_msg}')
        elif game_board[3]==f'\n{player_1_symbol}' and game_board[4]==player_1_symbol and game_board[5]==player_1_symbol:
            sys.exit(f'{player_1_won_msg}')
        elif game_board[3]==f'\n{player_2_symbol}' and game_board[4]==player_2_symbol and game_board[5]==player_2_symbol:
            sys.exit(f'{player_2_won_msg}')
        elif game_board[6]==f'\n{player_1_symbol}' and game_board[7]==player_1_symbol and game_board[8]==player_1_symbol:
            sys.exit(f'{player_1_won_msg}')
        elif game_board[6]==f'\n{player_2_symbol}' and game_board[7]==player_2_symbol and game_board[8]==player_2_symbol:
            sys.exit(f'{player_2_won_msg}')
        elif game_board[0]==player_1_symbol and game_board[3]==f'\n{player_1_symbol}' and game_board[6]==f'\n{player_1_symbol}':
            sys.exit(f'{player_1_won_msg}')
        elif game_board[0]==player_2_symbol and game_board[3]==f'\n{player_2_symbol}' and game_board[6]==f'\n{player_2_symbol}':
            sys.exit(f'{player_2_won_msg}')
        elif game_board[1]==player_1_symbol and game_board[4]==player_1_symbol and game_board[7]==player_1_symbol:
            sys.exit(f'{player_1_won_msg}')
        elif game_board[1]==player_2_symbol and game_board[4]==player_2_symbol and game_board[7]==player_2_symbol:
            sys.exit(f'{player_2_won_msg}')
        elif game_board[2]==player_1_symbol and game_board[5]==player_1_symbol and game_board[8]==player_1_symbol:
            sys.exit(f'{player_1_won_msg}')
        elif game_board[2]==player_2_symbol and game_board[5]==player_2_symbol and game_board[8]==player_2_symbol:
            sys.exit(f'{player_2_won_msg}')
        elif game_board[0]==player_1_symbol and game_board[4]==player_1_symbol and game_board[8]==player_1_symbol:
            sys.exit(f'{player_1_won_msg}')
        elif game_board[0]==player_2_symbol and game_board[4]==player_2_symbol and game_board[8]==player_2_symbol:
            sys.exit(f'{player_2_won_msg}') 
        elif game_board[2]==player_1_symbol and game_board[4]==player_1_symbol and game_board[6]==f'\n{player_1_symbol}':
            sys.exit(f'{player_1_won_msg}')
        elif game_board[2]==player_2_symbol and game_board[4]==player_2_symbol and game_board[6]==f'\n{player_2_symbol}':
            sys.exit(f'{player_2_won_msg}')
        else:
            print(f'{tie_msg}')
    try:
        player_1_name=input('Player 1 name:')
        time.sleep(1)
        player_2_name=input('Player 2 name:')
        time.sleep(1)
        symbol=input(f'What symbol do you want to be, {player_1_name}, {o} or {x}:')
        if symbol==x or symbol==x.lower() or symbol==o or symbol==o.lower():
            time.sleep(1)
            print(f'{player_1_name} chose {symbol}')
            if symbol==x or symbol==x.lower():
                time.sleep(1)
                print(f'Since {player_1_name} chose {symbol}, {player_2_name} will be {o}')
                opponent_symbol=o
            elif symbol==o or symbol==o.lower():
                time.sleep(1)
                print(f'Since {player_1_name} chose {symbol}, {player_2_name} will be {x} ')
                opponent_symbol=x
            def choose_position(player_1,player_2):
                if player_1:
                    player_1_turn=f'It is now {player_1_name}"s turn'
                    print(f'{player_1_turn}')
                    time.sleep(1)
                    position=int(input('Enter a number between 0 and 8: '))
                    if position>8 or position<0:
                        error_msg('Error, invalid index, pls restart the game')
                    elif position==3 or position==6:
                        del game_board[position] 
                        game_board.insert(position,f'\n{symbol}')
                        print(f'{" ".join(game_board)}')
                    else:
                        del game_board[position]
                        game_board.insert(position,symbol)
                        print(f'{" ".join(game_board)}')
                elif player_2:
                    print(f'It"s now {player_2_name}"s turn')
                    time.sleep(1)
                    position=int(input('Enter a number between 0 and 8:'))
                    if position>8 or position<0:
                        error_msg('Error, invalid index, pls restart the game')
                    elif position==3 or position==6:
                        del game_board[position]
                        game_board.insert(position,f'\n{opponent_symbol}')
                        print(f'{" ".join(game_board)}')
                    else:
                        del game_board[position]
                        game_board.insert(position,f'{opponent_symbol}')
                        print(f'{" ".join(game_board)}')
                        
            choose_position(player_1=player_1_name,player_2=player_2_name)
            if opponent_symbol not in game_board[:]:
                choose_position(player_1=None,player_2=player_2_name)
                choose_position(player_1=player_1_name,player_2=None)
                choose_position(player_1=None,player_2=player_2_name)
                choose_position(player_1=player_1_name,player_2=None)
                win_condition(player_1_symbol=symbol,player_2_symbol=opponent_symbol)
                choose_position(player_1=None,player_2=player_2_name)
                win_condition(player_1_symbol=symbol,player_2_symbol=opponent_symbol)
                choose_position(player_1=player_1_name,player_2=None)
                choose_position(player_1=None,player_2=player_2_name)
        else:
            error_msg(txt='Error, invalid symbol, pls restart the game')
    except ValueError:
        pass
    except IndexError:
        pass