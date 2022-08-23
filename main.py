from flask import Flask
from minha_aplicacao.views import minha_aplicacao_bp
from home.home import home_bp
from flask import session

app = Flask(__name__)
app.secret_key = "(B3nt0712)"

app.register_blueprint(minha_aplicacao_bp)
app.register_blueprint(home_bp)

if __name__ == '__main__':
    app.run(debug=True)
