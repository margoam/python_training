from model.contact import Contact
import random
import time


def test_edit_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Test_name23", middle_name="Test_middle_name2", last_name="Test_last_name",
                                   address="Belarus, Brest", home_number="123", mobile_number="+2342432432",
                                   birth_day="15", birth_month="July", birth_year="1993", second_number="+31231231"))
    old_contacts = db.get_contact_list()
    contacts = random.choice(old_contacts)
    contact = Contact(first_name="Test_name_new", last_name="Test_last_name_new", nick_name="test@@123",
                      home_number="+234234243", email="example@gmail.com", notes="text", birth_day="2", birth_month="June", birth_year="1976")
    contact.id = contacts.id
    app.contact.edit_random_contact_by_id(contacts.id, contact)
    time.sleep(1)
    new_contacts = db.get_contact_list()
    assert len(new_contacts) == len(old_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
