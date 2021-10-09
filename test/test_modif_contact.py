from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(first_name="Marta", middle_name="", last_name="Edit_Last_Name",
                             nick_name="test_nick_@@@", address="", home_number="+234234243", mobile_number="",
                             birth_day="", birth_month="", birth_year="", company="OOO TEST", title="Title_test",
                             email="example@gmail.com", address_sec="Belarus, Minsk", notes="text"))
    app.session.logout()
