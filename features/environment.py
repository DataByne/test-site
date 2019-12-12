from splinter import Browser
from behave import fixture, use_fixture
from behave.fixture import use_fixture_by_tag, fixture_call_params
from blogsite import db, create_app
from blogsite.models import User, Post
from config import TestConfig


@fixture
def splinter_browser( context, type='chrome' ):
	"""Sets up a splinter browser session

	Generator function that provides a web driver browser object for use in
	testing. The browser defaults to a Chrome web driver.

	Args:
		context:        Behave testing context
		type:           Specific webdriver to run

	Yields:
		A browser object attribute to the Behave testing module's context. The
		type of the browser is set to whichever the generator is provided.
	"""
	if type != 'flask':
		context.browser = Browser( driver_name=type )
	else:
		context.browser = Browser( driver_name=type, app=create_app( TestConfig ) )
	yield context.browser
	context.browser.quit()


@fixture
def flask_client( context, *args, **kwargs ):
	"""Sets up temporary flask context

	Generator function.

	Yields:
		A flask testing client attribute to Behave's context.
	"""
	app = create_app( TestConfig )
	# context.client = app.test_client()
	# context.client = create_app( TestConfig )
	with app.test_client() as testClient:
		# with app.app_context():
		context.client = testClient
		yield context.client


tag_registry = {
	"fixture.browser.chrome": fixture_call_params( splinter_browser ),
	"fixture.browser.flask": fixture_call_params( splinter_browser, type='flask' ),
	"fixture.flask": fixture_call_params( flask_client )
}

def before_all( context ):
	"""Runs before each test
	
	Args:
		context:	Behave testing context
	"""
	# use_fixture( flask_client, context )


def before_tag( context, tag ):
	"""Modifies context based on encountered tags
	
	Description
	
	Args:
		context:	Behave testing context
		tag:		Decorator tag from a feature file
	"""
	if tag.startswith( "fixture." ):
		return use_fixture_by_tag( tag, context, tag_registry )


# def after_all( context ):
	