# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save_note():
    content = request.form['note']
    with open('note.txt', 'w') as f:
        f.write(content)
    return "Note saved successfully!"

if __name__ == '__main__':
    app.run(debug=True)