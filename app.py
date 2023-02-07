from flask import Flask, request, redirect, render_template
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    host="localhost",
    database="mydatabase",
    user="postgres",
    password="secretpassword"
)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'")
        user = cursor.fetchone()

        if user:
            return redirect('/welcome')
        else:
            return redirect('/')

    return render_template('login.html')

@app.route('/welcome')
def welcome():
    return 'Welcome!'

if __name__ == '__main__':
    app.run()