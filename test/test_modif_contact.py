from model.contact import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(first_name="Marta", middle_name="-", last_name="Jons",
                             nick_name="12312@@@", address="Minsk", home_number="+21312313", mobile_number="+12313",
                             birth_day="5", birth_month="March", birth_year="1960"))
    app.session.logout()
