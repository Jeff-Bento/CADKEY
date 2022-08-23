from flask import Blueprint, session, abort


home_bp = Blueprint('home',__name__)

@home_bp.route('/home/')
def home():
    if session:
        print(session)
        return '<h1> Minha Pagina Home </h1> <br> <a href="/logout">Logout </a>'
    else:
        return abort(404,"Page Not Found")
