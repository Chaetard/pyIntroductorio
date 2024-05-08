from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='dbpython'
    )
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuario1')
    results = cursor.fetchall()
    conn.close()
    return str( results )


@app.route('/secon')
def secondary():
    
    return str("<h1>holaz<h1>")

if __name__ == '__main__':
    app.run(debug=True)