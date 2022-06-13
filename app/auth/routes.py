from flask import Blueprint, render_template


auth = Blueprint('auth', __name__, template_folder='auth_templates', url_prefix='/auth')

from .authforms import LoginForm

@auth.route('/login')
def login():
    lform = LoginForm()
    return render_template('login.html', form=lform)


