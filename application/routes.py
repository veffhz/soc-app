from flask import render_template, url_for, flash
from flask_login import login_required, current_user
from werkzeug.utils import redirect

from application import app
from application.dao import get_accounts, get_friends, get_account, update_account
from application.forms import ProfileForm


@app.route('/profile/')
@login_required
def profile():
    account = get_account(current_user.username)
    form = ProfileForm(data=account)
    return render_template("profile.html", form=form)


@app.route('/profile', methods=['POST'])
@login_required
def post_profile():
    form = ProfileForm()
    if form.validate_on_submit():
        password = form.password.data

        if current_user.password == password:
            updated_profile = form.populate_profile()
            update_account(updated_profile, current_user.user_id)
            flash('Изменения сохранены!', 'success')
            return redirect(url_for('profile'))
        else:
            flash('Неверный пароль!', 'warning')
    return render_template('profile.html', form=form)


@app.route('/users')
@login_required
def users():
    accounts = get_accounts()
    return render_template('users.html', users=accounts)


@app.route('/friends')
@login_required
def friends():
    users_data = get_friends(current_user.user_id)
    return render_template('friends.html', users=users_data)


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html')
