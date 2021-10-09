from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(nick_name="test@@123", home_number="+234234243", birth_day="6", birth_month="March", birth_year="1990",
                             company="OOO TEST", title="Title_test", email="example@gmail.com",
                             address_sec="Belarus, Minsk", notes="text"))
    app.session.logout()
