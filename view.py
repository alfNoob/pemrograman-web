from flask import render_template

class MahasiswaView:
    @staticmethod
    def index(data):
        return render_template('index.html', data=data)

    @staticmethod
    def tambah():
        return render_template('tambah.html')

    @staticmethod
    def edit(data):
        return render_template('edit.html', data=data)
