from flask import Flask, request, redirect, url_for
from flask_mysqldb import MySQL
from model import MahasiswaModel
from view import MahasiswaView

app = Flask(__name__, template_folder='templates')

# Konfigurasi MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db_mahasiswa'

mysql = MySQL(app)
mahasiswa_model = MahasiswaModel(mysql)
mahasiswa_view = MahasiswaView()

@app.route('/')
def index():
    data = mahasiswa_model.get_all()
    return mahasiswa_view.index(data)

@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        nama = request.form['nama']
        hobi = request.form['hobi']
        mahasiswa_model.create(nama, hobi)
        return redirect(url_for('index'))
    return mahasiswa_view.tambah()

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    data = mahasiswa_model.get_by_id(id)
    if request.method == 'POST':
        nama = request.form['nama']
        hobi = request.form['hobi']
        mahasiswa_model.update(id, nama, hobi)
        return redirect(url_for('index'))
    return mahasiswa_view.edit(data)

@app.route('/hapus/<int:id>')
def hapus(id):
    mahasiswa_model.delete(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
