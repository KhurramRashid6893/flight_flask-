from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Create a database to store customer preferences
def init_db():
    conn = sqlite3.connect('airline.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS preferences 
                 (id INTEGER PRIMARY KEY, name TEXT, email TEXT, seat TEXT, meal TEXT)''')
    conn.commit()
    conn.close()

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit_preferences', methods=['POST'])
def submit_preferences():
    name = request.form['name']
    email = request.form['email']
    seat = request.form['seat']
    meal = request.form['meal']

    conn = sqlite3.connect('airline.db')
    c = conn.cursor()
    c.execute('INSERT INTO preferences (name, email, seat, meal) VALUES (?, ?, ?, ?)', 
              (name, email, seat, meal))
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))

# Initialize the database
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
