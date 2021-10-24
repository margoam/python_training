from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="Test_name", middle_name="Test_middle_name", last_name="Test_last_name",
                      address="asdasdasd", home_number="123", mobile_number="131231231",
                      birth_day="3", birth_month="March", birth_year="1996")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
