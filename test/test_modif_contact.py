from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Test_name23", middle_name="Test_middle_name2", last_name="Test_last_name",
                                   address="Belarus, Brest", home_number="123", mobile_number="+2342432432",
                                   birth_day="15", birth_month="July", birth_year="1993"))
    app.contact.edit(Contact(nick_name="test@@123", home_number="+234234243", birth_day="9", birth_month="June",
                             birth_year="1990", email="example@gmail.com", notes="text"))
