from behave import *
from BrainBucketTest.pages.login_page import LoginPage
from BrainBucketTest.pages.registration_page import RegistrationPage


@given("user on the registration page")
def open_registration_page(context):
    login_page = LoginPage(context.browser)
    login_page.click_continue_btn()


@when('user types "{value}" in "{field}"')
def type_value_in_field(context, value, field):
    registration_page = RegistrationPage(context.browser)
    context.registration_form = registration_page

    if value == "None":
        return

    if field == "first_name":
        registration_page.enter_first_name(value)
    elif field == "last_name":
        registration_page.enter_last_name(value)
    elif field == "phonenumber":
        registration_page.enter_telephone(value)
    elif field == "password":
        registration_page.enter_password(value)


@when("user clicks Continue button")
def press_contninue_on_registration_form(context):
    context.registration_form.submit_form()


@then('error is shown under "{field}" field')
def verify_error_registration_form(context, field):
    if field == "first_name":
        assert context.registration_form.get_firstname_error() == "First Name must be between 1 and 32 characters!"
    elif field == "last_name":
        assert context.registration_form.get_lastname_error() == "Last Name must be between 1 and 32 characters!"
    elif field == "phonenumber":
        assert context.registration_form.get_phonenumber_error() == "Telephone must be between 3 and 32 characters!"
    elif field == "password":
        assert context.registration_form.get_password_error() == "Password must be between 4 and 20 characters!"
