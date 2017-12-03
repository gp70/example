#This function will record the number of times a player chose rock, paper, or scissors.

def RPC_data(player_choice):
    R_count=0
    P_count=0
    S_count=0
    if player_choice=='Rock':
        R_count+=1
    elif player_choice=='Paper':
        P_count+=1
    elif player_choice=='Scissor':
        S_count+=1
    