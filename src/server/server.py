from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

# Подключение к базе данных
def get_db_connection():
    conn = psycopg2.connect(
        dbname="2024_psql_dan", user="2024_psql_d_usr", password="hq7L54hC9LEc7YzC", host="5.183.188.132"
    )
    return conn

# Получение всех телефонов
@app.route('/phones', methods=['GET'])
def get_phones():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM phones;')
    phones = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(phones)

# Добавление телефона
@app.route('/phones', methods=['POST'])
def add_phone():
    new_phone = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO phones (name_phone, os_phone) VALUES (%s, %s) RETURNING id_phone;',
                (new_phone['name_phone'], new_phone['os_phone']))
    phone_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'id_phone': phone_id}), 201

# Обновление телефона
@app.route('/phones/<int:id_phone>', methods=['PUT'])
def update_phone(id_phone):
    updated_phone = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE phones SET name_phone = %s, os_phone = %s WHERE id_phone = %s;',
                (updated_phone['name_phone'], updated_phone['os_phone'], id_phone))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'status': 'updated'}), 200

# Удаление телефона
@app.route('/phones/<int:id_phone>', methods=['DELETE'])
def delete_phone(id_phone):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM phones WHERE id_phone = %s;', (id_phone,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'status': 'deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)