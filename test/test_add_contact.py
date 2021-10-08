from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="Test_name", middle_name="Test_middle_name", last_name="Test_last_name",
                               nick_name="", address="asdasdasd", home_number="123", mobile_number="131231231",
                               birth_day="3", birth_month="March", birth_year="1996", company="", title="",
                               email="", address_sec="", notes=""))
    app.session.logout()
