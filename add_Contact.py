import pytest
from contact import Contact
from contact_app import Contact_app


@pytest.fixture
def app_c(request):
    fixture = Contact_app()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app_c):
    app_c.login(username="admin", password="secret")
    app_c.create_contact(Contact(first_name="Test_name", middle_name="Test_middle_name", last_name="Test_last_name",
                        address="asdasdasd", home_number="123", mobile_number="131231231", birth_day="3",
                        birth_month="March", birth_year="1996"))
    app_c.logout()
