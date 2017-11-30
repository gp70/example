from random import random
weights = {'Normal Weights':(R,P,S),
           'Rock Focused':(R,R,P,S),
           'Paper Focused':(R,P,P,S),
           'Scissors Focused':(R,P,S,S)}
p_choice = ''
c_choice = ''
p_count = 0
c_count = 0

def decision(p,c):
    if (p == 'R'):
        if (c == 'R'):
        if (c == 'P'):
            c_count += 1
        if (c == 'S'):
            p_count += 1
    if (p == 'P'):
        if (c == 'R'):
            p_count += 1
        if (c == 'P'):
        if (c == 'S'):
            c_count += 1
    if (p == 'S'):
        if (c == 'R'):
            c_count += 1
        if (c == 'P'):
            p_count += 1
        if (c == 'S'):