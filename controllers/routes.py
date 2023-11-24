from flask import render_template, request, url_for, redirect
from models.database import db, Yup

def init_app(app):
    @app.route('/')
    def index():
        cookies = Yup.query.all()
        return render_template('index.html', cookies=cookies)

    # O GET é usado para abrir a página add.html e o POST para salvar os dados
    @app.route('/add', methods=['GET','POST'])
    def add():
        if request.method == 'POST':
            cookies = Yup(request.form['nome'], request.form['descricao'], request.form['preco'], request.form['imagem'])
            db.session.add(cookies)
            db.session.commit()
            return redirect(url_for('admin'))
        return render_template('add.html')
    
    @app.route('/admin')
    def admin():
        cookies = Yup.query.all()
        return render_template('admin.html', cookies=cookies)