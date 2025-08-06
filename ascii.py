import time
from colorama import Fore
import sys
import os
title='tic tac toe'
x='x'.upper()
o='o'.upper()
frames=[f'''
         {Fore.RED}██                        {Fore.BLUE}██{Fore.RESET}





████████╗  ╗ ██████╗    ████████╗██   ██╗  ██████╗   ████████╗ ██████╗ ███████╗
╚══██╔══╝██║██╔════╝    ╚══██╔══╝██╔══██╗██╔════╝    ╚══██╔══╝██╔═══██╗██╔════╝
   ██║   ██║██║            ██║   ███████║██║            ██║   ██║   ██║█████╗
   ██║   ██║██║            ██║   ██╔══██║██║            ██║   ██║   ██║██╔══╝
   ██║   ██║╚██████╗       ██║   ██║  ██║╚██████╗       ██║   ╚██████╔╝███████╗
   ╚═╝   ╚═╝ ╚═════╝       ╚═╝   ╚═╝  ╚═╝ ╚═════╝       ╚═╝    ╚═════╝ ╚══════╝''',

     f'''

         {Fore.RED}██                        {Fore.BLUE}██{Fore.RESET}


████████╗  ╗ ██████╗    ████████╗██   ██╗ ██████╗    ████████╗ ██████╗ ███████╗
╚══██╔══╝██║██╔════╝    ╚══██╔══╝██╔══██╗██╔════╝    ╚══██╔══╝██╔═══██╗██╔════╝
   ██║   ██║██║            ██║   ███████║██║            ██║   ██║   ██║█████╗
   ██║   ██║██║            ██║   ██╔══██║██║            ██║   ██║   ██║██╔══╝
   ██║   ██║╚██████╗       ██║   ██║  ██║╚██████╗       ██║   ╚██████╔╝███████╗
   ╚═╝   ╚═╝ ╚═════╝       ╚═╝   ╚═╝  ╚═╝ ╚═════╝       ╚═╝    ╚═════╝ ╚══════╝

                                   ''',f'''


         {Fore.RED}██                        {Fore.BLUE}██{Fore.RESET}
████████╗  ╗ ██████╗    ████████╗██   ██╗ ██████╗    ████████╗ ██████╗ ███████╗
╚══██╔══╝██║██╔════╝    ╚══██╔══╝██╔══██╗██╔════╝    ╚══██╔══╝██╔═══██╗██╔════╝
   ██║   ██║██║            ██║   ███████║██║            ██║   ██║   ██║█████╗
   ██║   ██║██║            ██║   ██╔══██║██║            ██║   ██║   ██║██╔══╝
   ██║   ██║╚██████╗       ██║   ██║  ██║╚██████╗       ██║   ╚██████╔╝███████╗
   ╚═╝   ╚═╝ ╚═════╝       ╚═╝   ╚═╝  ╚═╝ ╚═════╝       ╚═╝    ╚═════╝ ╚══════╝



                                 ''',f'''


████████╗{Fore.RED}██╗{Fore.RESET} ██████╗    ███{Fore.BLUE}██{Fore.RESET}███╗██████╗ ██████╗     ████████╗ ██████╗ ███████╗
╚══██╔══╝██║██╔════╝    ╚══██╔══╝██╔══██╗██╔════╝    ╚══██╔══╝██╔═══██╗██╔════╝
   ██║   ██║██║            ██║   ███████║██║            ██║   ██║   ██║█████╗
   ██║   ██║██║            ██║   ██╔══██║██║            ██║   ██║   ██║██╔══╝
   ██║   ██║╚██████╗       ██║   ██║  ██║╚██████╗       ██║   ╚██████╔╝███████╗
   ╚═╝   ╚═╝ ╚═════╝       ╚═╝   ╚═╝  ╚═╝ ╚═════╝       ╚═╝    ╚═════╝ ╚══════╝

        ''']
def error_msg(txt=''):
    for text in txt:
        sys.stderr.flush()
        time.sleep(0.1)
        sys.stderr.write(f'{Fore.RED}{text}')
    else:
        global reset_to_default_color
        reset_to_default_color=Fore.RESET
        print(f'{reset_to_default_color}')
for txt in frames:
    sys.stdout.flush()
    time.sleep(1)
    os.system("cls")
    sys.stdout.write(txt)
else:
    time.sleep(1)
    os.system("cls")
    print(f'{Fore.WHITE}')
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
        global player_1_won_msg
        player_1_won_msg='PLayer 1 won!'
        global player_2_won_msg
        player_2_won_msg='Player 2 won!'
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
        elif '-' not in game_board:
            sys.exit("DRAW")
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
                    position=int(input('Enter a number between 1 and 9: '))
                    if position>9 or position<1:
                        error_msg('Error, invalid index, pls restart the game')
                    elif position==1 and game_board[0]==opponent_symbol or position==2 and game_board[1]==opponent_symbol or position==3 and game_board[2]==opponent_symbol or position==4 and game_board[3]==f"\n{opponent_symbol}" or position==5 and game_board[4]==opponent_symbol or position==6 and game_board[5]==opponent_symbol or position==7 and game_board[6]==f"\n{opponent_symbol}" or position==8 and game_board[7]==opponent_symbol or position==9 and game_board[8]==opponent_symbol:
                          quit("cannot perform action due to the desired space being occupied by player 2's symbol.")
                    elif position==1 and game_board[0]==symbol or position==2 and game_board[1]==symbol or position==3 and game_board[2]==symbol or position==4 and game_board[3]==f"\n{symbol}" or position==5 and game_board[4]==symbol or position==6 and game_board[5]==symbol or position==7 and game_board[6]==f"\n{symbol}" or position==8 and game_board[7]==symbol or position==9 and game_board[8]==symbol:
                          quit("space is already taken by your symbol player 1.")
                    elif position==7 or position==4:
                        del game_board[position-1]
                        game_board.insert(position-1,f'\n{symbol}')
                        print(f'{" ".join(game_board)}')
                    else:
                        del game_board[position-1]
                        game_board.insert(position-1,symbol)
                        print(f'{" ".join(game_board)}')
                elif player_2:
                    print(f'It"s now {player_2_name}"s turn')
                    time.sleep(1)
                    position=int(input('Enter a number between 1 and 9:'))
                    if position>9 or position<1:
                        error_msg('Error, invalid index, pls restart the game')
                    elif position==1 and game_board[0]==symbol or position==2 and game_board[1]==symbol or position==3 and game_board[2]==symbol or position==4 and game_board[3]==f"\n{symbol}" or position==5 and game_board[4]==symbol or position==6 and game_board[5]==symbol or position==7 and game_board[6]==f"\n{symbol}" or position==8 and game_board[7]==symbol or position==9 and game_board[8]==symbol:
                          quit("cannot perform action due to the desired space being occupied by player 1's symbol")
                    elif position==1 and game_board[0]==opponent_symbol or position==2 and game_board[1]==opponent_symbol or position==3 and game_board[2]==opponent_symbol or position==4 and game_board[3]==f"\n{opponent_symbol}" or position==5 and game_board[4]==opponent_symbol or position==6 and game_board[5]==opponent_symbol or position==7 and game_board[6]==f"\n{opponent_symbol}" or position==8 and game_board[7]==opponent_symbol or position==9 and game_board[8]==opponent_symbol:
                          quit("space is already taken by your symbol player 1.")
                    elif position==7 or position==4:
                        del game_board[position-1]
                        game_board.insert(position-1,f'\n{opponent_symbol}')
                        print(f'{" ".join(game_board)}')
                    else:
                        del game_board[position-1]
                        game_board.insert(position-1,f'{opponent_symbol}')
                        print(f'{" ".join(game_board)}')

            choose_position(player_1=player_1_name,player_2=player_2_name)
            while "-" in game_board[:] or "\n-" in game_board:
                choose_position(player_1=None,player_2=player_2_name)
                win_condition(player_1_symbol=symbol,player_2_symbol=opponent_symbol)
                choose_position(player_1=player_1_name,player_2=None)
                win_condition(player_1_symbol=symbol,player_2_symbol=opponent_symbol)
        else:
            sys.exit(error_msg(txt='Error, invalid symbol, pls restart the game'))
    except ValueError:
        sys.exit("ValueError occurred.")
