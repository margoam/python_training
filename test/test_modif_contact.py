from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.edit(Contact(nick_name="test@@123", home_number="+234234243", birth_day="9", birth_month="June",
                             birth_year="1990", email="example@gmail.com", notes="text"))
