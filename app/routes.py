from flask import render_template
from app import app

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