from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Test_name23", middle_name="Test_middle_name2", last_name="Test_last_name",
                                   address="Belarus, Brest", home_number="123", mobile_number="+2342432432",
                                   birth_day="15", birth_month="July", birth_year="1993"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="Test_name_new", last_name="Test_last_name_new", nick_name="test@@123",
                      home_number="+234234243", email="example@gmail.com", notes="text", birth_day="2", birth_month="June", birth_year="1976")
    contact.id = old_contacts[0].id
    app.contact.edit(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
