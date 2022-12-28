from behave import given, when, then
from BrainBucketTest.utils.config_reader import ConfigReader
from BrainBucketTest.drivers.browser import Browser
from BrainBucketTest.pages.login_page import LoginPage
from BrainBucketTest.pages.profile_page import ProfilePage


URL = "https://techskillacademy.net/brainbucket/index.php?route=account/login"
configs = ConfigReader("BrainBucketTests/BDDBehave/logintests/steps/config.ini")


@given("user launch login page")
def launch_login_page(context):
    browser = Browser(URL, configs.get_browser(), configs.get_wait_time())
    context.browser = browser


@given("user is not logged in")
def verify_user_not_logged_in(context):
    login_page = LoginPage(context.browser)
    assert login_page.get_new_customer_title() == "New Customer"
    assert login_page.get_returning_customer_title() == "Returning Customer"
    context.login_page = login_page


@when("user enters email and password")
def enter_email_and_password(context):
    login_page = context.login_page
    login_page.email_input_click(configs.get_user1_email())
    login_page.password_input_click(configs.get_user1_password())


@when('user clicks Login button')
def click_login_button(context):
    login_page = context.login_page
    login_page.click_login_button()


@then("user's profile page is launched")
def verify_user_profile_view(context):
    profile_page = ProfilePage(context.browser)
    assert profile_page.get_my_account_title() == "My Account"
    assert profile_page.get_my_orders_title() == "My Orders"
    assert profile_page.get_newsletter_title() == "Newsletter"

