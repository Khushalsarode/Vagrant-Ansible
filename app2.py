# app2.py
from flask import Flask
import pymysql

app = Flask(__name__)

# Database Configuration
db_config = {
    'user': 'app2_user',
    'password': 'app2_password',
    'host': 'database_host',
    'database': 'db_two',
}

@app.route('/db')
def db_api():
    # Connect to MySQL
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    # Perform a simple database query (replace with your actual query)
    cursor.execute('SELECT * FROM your_table;')
    result = cursor.fetchall()

    # Close the connection
    connection.close()

    return str(result)

@app.route('/non-db')
def non_db_api():
    return 'HTTP 200 OK'

if __name__ == '__main__':
    app.run(port=5001)