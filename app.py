from flask import Flask, render_template, request, redirect, url_for
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

name = ''
age = ''
gender = ''

@app.route('/', methods=['POST', 'GET'])
def main():
    # Initialization
    
    global pwcount,cwcount,tcount,prcount,ppcount,pscount,crcount,cpcount,cscount,name,age,gender
    
    if request.method == 'GET':
        return render_template('mainpage.html',name = name, age = age, gender = gender)
    
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
            
        if winner[0] == 'Player':
            winplayer = name
        if winner[0] != 'Player':
            winplayer = winner[0]
            
        return render_template('mainpage.html', choice = choice, cchoice = winner[1],
                                                winner = winplayer, prcount = prcount,
                                                ppcount = ppcount, pscount = pscount,
                                                crcount = crcount, cpcount = cpcount,
                                                cscount = cscount, pwcount = pwcount,
                                                cwcount = cwcount, tcount = tcount,
                                                name = name, age = age, gender = gender)
@app.route('/playerinfo', methods=['POST', 'GET'])

def Player_info():
    
    global pwcount, cwcount, tcount, prcount, ppcount, pscount, crcount, cpcount, cscount, name, age, gender
    
    if request.method == 'POST':
        
        name = request.form['Name']
        age = request.form['Age']
        gender = request.form.get('gender')
        
        return redirect(url_for('main'))
    
    if request.method=='GET':
        return render_template('Main.html')
    

app.run(debug=True,host='0.0.0.0',port=5000)
