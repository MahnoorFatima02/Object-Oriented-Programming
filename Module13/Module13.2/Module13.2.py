from flask import Flask, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'flightgameuser'
app.config['MYSQL_DATABASE_PASSWORD'] = '123Maa123'
app.config['MYSQL_DATABASE_DB'] = 'flight_game'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL(app)

# Route to fetch data from the database
@app.route('/airport/<ICAO_code>', methods=['GET'])
def airport(ICAO_code):
    try:
        # Create a MySQL cursor
        cur = mysql.get_db().cursor()

        # Execute a sample query
        cur.execute("SELECT ident, name, municipality FROM airport WHERE ident = '" + ICAO_code + "'")

        # Fetch all rows from the query result
        data = cur.fetchall()
        result = {}
        result['ICAO'] = data[0][0]
        result['Name'] = data[0][1]
        result['Location'] = data[0][2]

        return result

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
