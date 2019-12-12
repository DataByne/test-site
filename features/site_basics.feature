Feature: site basic navigation
	Simple tests to ensure that the site is building properly without delving
	into operations very deeply.
	
	@fixture.browser.flask	
	Scenario: home page is able to load in flask browser
		Given we are looking at the home page
		Then the page contains "Home"
		
	