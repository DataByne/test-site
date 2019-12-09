from site import app, db
from site.models import User, Post

@app.shell_context_processor
def make_shell_context():
	return { 'db': db, 'User': User, 'Post': Post }

