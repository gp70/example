import random

def refine(p,w):
    weights = {'normal weights':('R','P','S'),
               'rock focused':('R','R','P','S'),
               'paper focused':('R','P','P','S'),
               'scissors focused':('R','P','S','S')}
    wlist = []
    for key in weights:
        wlist.append(key)
    if w.lower() not in wlist:
        w = 'Normal Weights'
    if p.lower() == 'rock':
        return decision('R',random.choice(weights[w.lower()]))
    if p.lower() == 'paper':
        return decision('P',random.choice(weights[w.lower()]))
    if p.lower() == 'scissors':
        return decision('S',random.choice(weights[w.lower()]))
    return 'Type \"Rock,\" \"Paper,\" or \"Scissors,\" please! Nobody'

def decision(p,c):
    p_count = 0
    c_count = 0
    if (p == 'R'):
        if (c == 'R'):
            return 'Nobody'
        if (c == 'P'):
            c_count += 1
            return 'Computer'
        if (c == 'S'):
            p_count += 1
            return 'Player'
    if (p == 'P'):
        if (c == 'R'):
            p_count += 1
            return 'Player'
        if (c == 'P'):
            return 'Nobody'
        if (c == 'S'):
            c_count += 1
            return 'Computer'
    if (p == 'S'):
        if (c == 'R'):
            c_count += 1
            return 'Computer'
        if (c == 'P'):
            p_count += 1
            return 'Player'
        if (c == 'S'):
            return 'Nobody'