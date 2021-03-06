from pytest import mark
from model.contact import Contact
import re


def test_contacts_on_home_page(app, db):
    contact_from_home_page = app.contact.get_contact_list()
    contact_from_db = db.get_contact_list()
    contact_from_db.sort(key=Contact.id_or_max)
    contact_from_home_page.sort(key=Contact.id_or_max)
    # параллельное сравнение полей контактов (телефонов и емейлов)
    for i, k in zip(contact_from_db, contact_from_home_page):
        assert merge_phones(i) == k.all_phones_from_home_page
        assert merge_emails(i) == k.all_emails_from_home_page
    assert contact_from_home_page == contact_from_db

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
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None, [contact.email, contact.email2,
                                                                                contact.email3])))
