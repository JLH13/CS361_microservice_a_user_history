from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            from_currency TEXT NOT NULL,
            to_currency TEXT NOT NULL,
            amount REAL NOT NULL,
            result REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/add_conversion', methods=['POST'])
def add_conversion():
    data = request.get_json()
    user_id = data['user_id']
    from_currency = data['from_currency']
    to_currency = data['to_currency']
    amount = data['amount']
    result = data['result']

    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO history (user_id, from_currency, to_currency, amount, result)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_id, from_currency, to_currency, amount, result))
    conn.commit()
    conn.close()

    return jsonify({"Message": "Conversion added."})

@app.route('/get_history/<user_id>', methods=['GET'])
def get_history(user_id):
    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM history WHERE user_id = ?
    ''', (user_id,))
    rows = cursor.fetchall()
    conn.close()

    history = []
    for row in rows:
        history.append({
            "id": row[0],
            "user_id": row[1],
            "from_currency": row[2],
            "to_currency": row[3],
            "amount": row[4],
            "result": row[5],
            "timestamp": row[6]
        })

    return jsonify(history)

@app.route('/reset_history', methods=['POST'])
def reset_history():
    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS history')
    cursor.execute('''
        CREATE TABLE history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            from_currency TEXT NOT NULL,
            to_currency TEXT NOT NULL,
            amount REAL NOT NULL,
            result REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    return jsonify({"Message": "History reset."})

if __name__ == '__main__':
    app.run(debug=True)
