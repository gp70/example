from flask import Flask, render_template, request, redirect
import rps
app = Flask(__name__)

# Variables

pwcount = 0
cwcount = 0
tcount = 0
    
prcount = 0
ppcount = 0
pscount = 0
crcount = 0
cpcount = 0
cscount = 0

@app.route('/', methods=['POST', 'GET'])
def main():
    # Initialization
    
    global pwcount,cwcount,tcount,prcount,ppcount,pscount,crcount,cpcount,cscount
    
    if request.method == 'GET':
        return render_template('mainpage.html')
    
    # Input
    
    if request.method == 'POST':
        choice = request.form['choice']
        weight = request.form['weight']
        
        # Easter Egg
        if ('doot' in choice.lower()) or ('doot' in weight.lower()):
            return redirect('http://www.reddoot.com', code = 302)
        
        winner = rps.refine(choice,weight)
        
        if winner[0] == 'Player':
            pwcount += 1
        if winner[0] == 'Computer':
            cwcount += 1
        if winner[0] == 'Nobody':
            tcount += 1
            
        if choice.lower() == 'rock':
            prcount += 1
        if choice.lower() == 'paper':
            ppcount += 1
        if choice.lower() == 'scissors':
            pscount += 1
            
        if winner[1].lower() == 'rock':
            crcount += 1
        if winner[1].lower() == 'paper':
            cpcount += 1
        if winner[1].lower() == 'scissors':
            cscount += 1
            
        return render_template('mainpage.html', choice = choice, cchoice = winner[1],
                                                winner = winner[0], prcount = prcount,
                                                ppcount = ppcount, pscount = pscount,
                                                crcount = crcount, cpcount = cpcount,
                                                cscount = cscount, pwcount = pwcount,
                                                cwcount = cwcount, tcount = tcount)
    

app.run(debug=True,host='0.0.0.0',port=5000)