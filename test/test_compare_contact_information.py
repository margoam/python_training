from pytest import mark
from model.contact import Contact
from random import randrange
import re


def test_contacts_on_home_page(app, db):
    contact_from_home_page = app.contact.get_contact_list()
    contact_from_db = db.get_contact_list()
    merged_phones_db = []
    phones_ui = []
    merged_emails_db = []
    emails_ui = []
    for i in contact_from_db:
        merged_phones_db.append(merge_phones(i))
    for i in contact_from_home_page:
        phones_ui.append(i.all_phones_from_home_page)
    for i in contact_from_db:
        merged_emails_db.append(merge_emails(i))
    for i in contact_from_home_page:
        emails_ui.append(i.all_emails_from_home_page)
    assert sorted(contact_from_home_page, key=Contact.id_or_max) == sorted(contact_from_db, key=Contact.id_or_max)
    assert sorted(phones_ui) == sorted(merged_phones_db)
    assert sorted(emails_ui) == sorted(merged_emails_db)

@mark.skip(reason='not necessary')
def test_phones_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home_number == contact_from_edit_page.home_number
    assert contact_from_view_page.mobile_number == contact_from_edit_page.mobile_number
    assert contact_from_view_page.work_number == contact_from_edit_page.work_number
    assert contact_from_view_page.fax_number == contact_from_edit_page.fax_number


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x),
                                                   filter(lambda x: x is not None, [contact.home_number,
                                                                                    contact.mobile_number,
                                                                                    contact.work_number,
                                                                                    contact.second_number]))))


def merge_emails(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x),
                                                   filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))
