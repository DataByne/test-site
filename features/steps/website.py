import behave


@given(u'we are looking at the home page')
def step_impl(context):
    context.browser.visit( 'http://localhost:5000/' )


@then(u'the page contains "{text}"')
def step_impl( context, text ):
    assert context.browser.is_text_present( text )