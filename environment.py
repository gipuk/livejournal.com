from browser import Browser
from pages import login_page, new_post, settings

def before_all(context):
    context.browser = Browser()
    context.login = login_page.LoginPage()
    context.post = new_post.PostNewEntry()
    context.settings = settings.SettingsTab()

def after_all(context):
    context.browser.quit()