"""from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import bcrypt

app = Flask(__name__)
CORS(app)

db_config = {
    'user': 'root',  
    'password': 'Ahalyaravi@5114',  
    'host': 'localhost',
    'database': 'register'
}

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor(dictionary=True)  

            cursor.execute("SELECT username, email FROM users")
            users = cursor.fetchall()

            cursor.close()
            connection.close()

            if not users:
                return jsonify({"message": "No users found"}), 200

            return jsonify({"users": users}), 200

        except mysql.connector.Error as err:
            print(f"MySQL error: {err}")
            return jsonify({"message": f"Database error: {str(err)}"}), 500
        except Exception as e:
            print(f"Error occurred: {e}")
            return jsonify({"message": f"An error occurred: {str(e)}"}), 500

    if request.method == 'POST':
        try:
            data = request.json
            username = data['username']
            email = data['email']
            password = data['password']

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()

            cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                           (username, email, hashed_password.decode('utf-8')))
            connection.commit()

            cursor.close()
            connection.close()

            return jsonify({"message": "User registered successfully!"}), 201

        except mysql.connector.Error as err:
            print(f"MySQL error: {err}")
            return jsonify({"message": f"Database error: {str(err)}"}), 500
        except Exception as e:
            print(f"Error occurred: {e}")
            return jsonify({"message": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import bcrypt

app = Flask(__name__)
CORS(app)

db_config = {
    'user': 'root',
    'password': 'Ahalyaravi@5114',
    'host': 'localhost',
    'database': 'register'
}

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        username = data['username']
        email = data['email']
        password = data['password']

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                       (username, email, hashed_password.decode('utf-8')))
        connection.commit()

        cursor.close()
        connection.close()

        return jsonify({"message": "User registered successfully!"}), 201

    except mysql.connector.Error as err:
        print(f"MySQL error: {err}")
        return jsonify({"message": f"Database error: {str(err)}"}), 500
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

@app.route('/register', methods=['GET'])
def get_users():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        cursor.execute("SELECT id, username, email FROM users")
        users = cursor.fetchall()

        cursor.close()
        connection.close()

        users_list = [{"id": user[0], "username": user[1], "email": user[2]} for user in users]

        return jsonify(users_list), 200

    except mysql.connector.Error as err:
        print(f"MySQL error: {err}")
        return jsonify({"message": f"Database error: {str(err)}"}), 500
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
