from model.contact import Contact
from model.group import Group
import random


def test_del_contact_to_group(app, orm, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Test_name", middle_name="Test_middle_name", last_name="Test_last_name",
                                   address="asdasdasd", home_number="123", mobile_number="131231231",
                                   birth_day="3", birth_month="March", birth_year="1996"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test3", header="dsffsd", footer="sggsdgs"))
    contacts = db.get_contact_list()
    contact = random.choice(contacts)
    groups = db.get_group_list()
    group = random.choice(groups)
    contacts_in_group = orm.get_contacts_in_group(group)
    if contacts_in_group == []:
        app.contact.add_contact_to_group(contact.id, group.name)
    app.contact.del_contact_to_group(contact.id, group.name)
    contacts_in_group = orm.get_contacts_in_group(group)
    assert contact not in contacts_in_group
