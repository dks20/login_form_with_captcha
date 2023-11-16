from flask import Flask, render_template, request, redirect, url_for
import MySQLdb

app = Flask(__name__)

# Replace these credentials with your MySQL credentials
db = MySQLdb.connect(host="localhost", user="root", password="root12", database="user_auth", port=3306)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor = db.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        db.commit()
        cursor.close()

        return redirect(url_for('login'))

    return render_template('login.html')





if __name__ == '__main__':
    app.run(debug=True,host = '0.0.0.0' , port=5000)
