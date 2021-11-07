from model.contact import Contact
import random


def test_del_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Test_name", middle_name="Test_middle_name", last_name="Test_last_name",
                                   address="asdasdasd", home_number="123", mobile_number="131231231",
                                   birth_day="3", birth_month="March", birth_year="1996"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_random_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
