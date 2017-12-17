from behave import *


@given('user is logged in')
def step_impl(context):
    context.browser.open_home_page()
    context.login.login('NetguruTest', 'Netguru2017!')

@when('I click post new entry')
def step_impl(context):
    context.post.go_to_post_new_entry_page()

@when('I fill all fields')
def step_impl(context):
    context.post.close_popup()
    context.post.fill_fields('title1','text1')

@when('click Draft button')
def step_impl(context):
    context.post.go_to_draft()

@then('new entry post is saved as a draft')
def step_impl(context):
    context.post.saved_as_a_draft('title1')

@when('I enter settings')
def step_impl(context):
    context.settings.go_to_settings()

@when('I enter display tab')
def step_impl(context):
    context.settings.go_to_display()

@when('I change language to german')
def step_impl(context):
    context.settings.change_language('Deutsch')
    context.settings.save_settings()

@then('page is available in german')
def step_impl(context):
    context.settings.de_language_set()

@when('click Publish button')
def step_impl(context):
    context.post.published()

@then('there is an error message')
def step_impl(context):
    context.post.error()

@when('I enter history tab')
def step_impl(context):
    context.settings.go_to_history()

@then('Old session is closed')
def step_impl(context):
    context.settings.closed_session()
