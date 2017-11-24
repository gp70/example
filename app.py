from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('mainpage.html')

app.run(debug=True,host='0.0.0.0',port=5000)