from flask import Blueprint, render_template, request
from flask.helpers import flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean=True)


@auth.route('/logout')
def logout():
    return render_template("logout.html")


@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        first_name = data.get('firstName')
        password1 = data.get('password1')
        password2 = data.get('password2')
        if password1 != password2:
            flash('Password isn\'t equal', category='error')
        else:
            flash('Account created!', category='success')

    return render_template("sign_up.html")
