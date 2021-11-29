import time

from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, orm, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Test_name", middle_name="Test_middle_name", last_name="Test_last_name",
                                   address="asdasdasd", home_number="123", mobile_number="131231231",
                                   birth_day="3", birth_month="March", birth_year="1996"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test3", header="dsffsd", footer="sggsdgs"))
    contacts = db.get_contact_list()
    groups = db.get_group_list()
    selected_contact = None
    selected_group = None
    # поиск контакта, которого нет хотя бы в одной группе
    selected_contact, selected_group = app.contact.find_contact_not_in_group(contacts, groups, orm, selected_contact,
                                                                             selected_group)
    # если все доступные контакты уже добавлены во всевозможные группы
    if selected_group is None and selected_contact is None:
        # добавляем новый контакт, которого нет ни в какой группе
        app.contact.create(Contact(first_name="Test_name", middle_name="Test_middle_name", last_name="Test_last_name",
                                   address="asdasdasd", home_number="123", mobile_number="131231231",
                                   birth_day="3", birth_month="March", birth_year="1996"))
        contacts = db.get_contact_list()
        # выбор последнего добавленного контакта (нового) по наибольшему id
        selected_contact = max(contacts, key=Contact.id_or_max)
        # выбор последней добавленной группы (здесь неважно, есть ли в группе уже контакты)
        selected_group = max(groups, key=Group.id_or_max)
    app.contact.add_contact_to_group(selected_contact.id, selected_group.name)
    time.sleep(2)
    contacts_in_group = orm.get_contacts_in_group(selected_group)
    # проверка, что выбранный контакт находится в соответствующей группе
    assert selected_contact in contacts_in_group
