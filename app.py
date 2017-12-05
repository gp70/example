from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def main():
    # Initialization
    # Input
    if ("R" or "S" or "P" or "Do Something") in request.form:
        print("Success")
    return render_template('mainpage.html')

app.run(debug=True,host='0.0.0.0',port=5000)