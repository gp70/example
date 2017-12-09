import random

def refine(p,w):
    weights = {'normal':('R','P','S'),
               'rock focused':('R','R','P','S'),
               'paper focused':('R','P','P','S'),
               'scissors focused':('R','P','S','S'),
               'realistic':('R','R','R','R','R','R','R',
                            'P','P','P','P','P','P','P',
                            'S','S','S','S','S','S')}
    wlist = []
    for key in weights:
        wlist.append(key)
    if w.lower() not in wlist:
        w = 'Normal'
    if p.lower() == 'rock':
        return decision('R',random.choice(weights[w.lower()]))
    if p.lower() == 'paper':
        return decision('P',random.choice(weights[w.lower()]))
    if p.lower() == 'scissors':
        return decision('S',random.choice(weights[w.lower()]))
    return ('Type \"Rock,\" \"Paper,\" or \"Scissors,\" please! Nobody', 'Nothing')

def decision(p,c):
    if (p == 'R'):
        if (c == 'R'):
            return ('Nobody','Rock')
        if (c == 'P'):
            return ('Computer','Paper')
        if (c == 'S'):
            return ('Player','Scissors')
    if (p == 'P'):
        if (c == 'R'):
            return ('Player','Rock')
        if (c == 'P'):
            return ('Nobody','Paper')
        if (c == 'S'):
            return ('Computer','Scissors')
    if (p == 'S'):
        if (c == 'R'):
            return ('Computer','Rock')
        if (c == 'P'):
            return ('Player','Paper')
        if (c == 'S'):
            return ('Nobody','Scissors')