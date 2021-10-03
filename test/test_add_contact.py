import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(first_name="Test_name", middle_name="Test_middle_name", last_name="Test_last_name",
                        address="asdasdasd", home_number="123", mobile_number="131231231", birth_day="3",
                        birth_month="March", birth_year="1996"))
    app.session.logout()
