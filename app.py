from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def main():
    # Initialization
    if request.method == 'GET':
        return render_template('mainpage.html')
    # Input
    if request.method == 'POST':
        choice = request.form['choice']
        return render_template('mainpage.html',choice = choice)

app.run(debug=True,host='0.0.0.0',port=5000)