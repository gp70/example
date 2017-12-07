from flask import Flask, render_template, request
import rps
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def main():
    # Initialization
    if request.method == 'GET':
        return render_template('mainpage.html')
    # Input
    if request.method == 'POST':
        choice = request.form['choice']
        weight = request.form['weight']
        winner = rps.refine(choice,weight)
        return render_template('mainpage.html', choice = choice, winner = winner)

app.run(debug=True,host='0.0.0.0',port=5000)