import random

weights = {'Normal Weights':('R','P','S'),
           'Rock Focused':('R','R','P','S'),
           'Paper Focused':('R','P','P','S'),
           'Scissors Focused':('R','P','S','S')}
p_count = 0
c_count = 0

def refine(p):
    weights = {'Normal Weights':('R','P','S'),
               'Rock Focused':('R','R','P','S'),
               'Paper Focused':('R','P','P','S'),
               'Scissors Focused':('R','P','S','S')}
    if p == 'Rock':
        return decision('R',random.choice(weights['Normal Weights']))
    if p == 'Paper':
        return decision('P',random.choice(weights['Normal Weights']))
    if p == 'Scissors':
        return decision('S',random.choice(weights['Normal Weights']))
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