from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('cafes.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cafes = conn.execute('SELECT * FROM cafe').fetchall()
    conn.close()
    return render_template('index.html', cafes=cafes)


@app.route('/add', methods=('GET', 'POST'))
def add_cafe():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        conn = get_db_connection()
        conn.execute('INSERT INTO cafe (name, location) VALUES (?, ?)', (name, location))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_cafe.html')


@app.route('/delete/<int:id>')
def delete_cafe(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM cafe WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
