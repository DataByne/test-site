from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Dory'}
    posts = [
        {
            'author':   { 'username': 'Fred' },
            'body':     "It's a beautiful day in the neighborhood!"
        },
        {
            'author':   { 'username': 'Henry' },
            'body':     "And gentlemen in England now-a-bed shall think themselves accurs'd they were not here."
        }
    ]
    return render_template( 'index.html', title='Home', user=user, posts=posts )

# @app.route('/xlogin')
# def xlogin():
#     form = LoginForm()
#     return render_template('login.html', title='Sign In', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Generally get and post would be separate
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect( url_for('index') )
    return render_template('login.html', title='Sign In', form=form)