from blogsite import db, create_app
from blogsite.models import User, Post

def list_all_users():
	app = create_app()
	
	with app.app_context():
		users = User.query.all()
		for user in users:
			print( user.username )
		


def main():
	list_all_users()

if ( __name__ == '__main__' ):
	main()