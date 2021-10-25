from pytest import mark
from random import randrange
import re


def test_contacts_on_home_page(app):
    list_of_contacts = app.contact.get_contact_list()
    index = randrange(len(list_of_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page == contact_from_edit_page
    assert contact_from_home_page.all_phones_from_home_page == merge_phones(contact_from_edit_page)  # за исключением факса, так как он не отображается на главной странице
    assert contact_from_home_page.all_emails_from_home_page == merge_emails(contact_from_edit_page)


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
                                                                                    contact.work_number]))))


def merge_emails(contact):
    return "\n".join(filter(lambda x: x != "", [contact.email, contact.email2, contact.email3]))
