from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(first_name="Test_name", middle_name="Test_middle_name", last_name="Test_last_name",
                               address="asdasdasd", home_number="123", mobile_number="131231231",
                               birth_day="3", birth_month="March", birth_year="1996"))
    app.session.logout()
