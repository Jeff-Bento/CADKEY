from flask import Blueprint, render_template, request, redirect, url_for, abort, session, flash

minha_aplicacao_bp = Blueprint('minha_aplicacao', __name__)

@minha_aplicacao_bp.route('/')
def index():
    return render_template('index.html')

@minha_aplicacao_bp.route('/valida/',methods=['POST','GET'])
def valida():
    if request.method == 'POST':
        user = request.form['name']
        password = request.form['password']
        if user:
            print(f"{user} *********** {password}")
            session['users'] = user+password
            flash(user + ' logou com sucesso!')
            print(f"{session}")
            print(session.keys)
            return redirect('/home/')
    else:
        return abort(404,'Page Not Found')


@minha_aplicacao_bp.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')