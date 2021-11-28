from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'ebpm'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formSubmit', methods = ['POST', 'GET'])
def submitForm():
    if request.method == 'POST':
        noPO = request.form['noPO']
        namaProduk = request.form['namaProduk']
        jumlahProduk = request.form['jumlahProduk']
        dana = request.form['dana']
        hargaProduk = request.form['hargaProduk']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO penjualanKelompok1 VALUES(%s,%s,%s,%s,%s,%s)''',("1", noPO, namaProduk, jumlahProduk, dana, hargaProduk))
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"

app.run(host='localhost', port=5000)
        