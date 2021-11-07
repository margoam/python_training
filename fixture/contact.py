from model.contact import Contact
import re
import os.path
import json


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("results")) > 0):
            with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../target.json")) as f:  # .. -на один уровень выше
                target = json.load(f)
            wd.get(target['web']["baseUrl"])

    def fill_contact_form(self, contact):
        self.edit_name_field("firstname", contact.first_name)
        self.edit_name_field("middlename", contact.middle_name)
        self.edit_name_field("nickname", contact.nickname)
        self.edit_name_field("lastname", contact.last_name)
        self.edit_name_field("home", contact.home_number)
        self.edit_name_field("byear", contact.birth_year)
        self.edit_name_field("mobile", contact.mobile_number)
        self.edit_name_field("work", contact.work_number)
        self.edit_name_field("fax", contact.fax_number)
        self.edit_name_field("phone2", contact.second_number)
        self.edit_name_field("email", contact.email)
        self.edit_name_field("address", contact.address)
        self.edit_name_field("notes", contact.notes)
        self.edit_name_field("bday", contact.birth_day)
        self.edit_name_field("bmonth", contact.birth_month)

    def edit_name_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            if field_name not in ("bday", "bmonth"):
                wd.find_element_by_name(field_name).click()
                wd.find_element_by_name(field_name).clear()
                wd.find_element_by_name(field_name).send_keys(text)
            else:
                wd.find_element_by_name(field_name).click()
                wd.find_element_by_name(field_name).send_keys(text)

    def choose_first_contact_for_edit(self):
        self.choose_random_contact_for_edit(0)

    def choose_random_contact_for_edit(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def create(self, contact):
        wd = self.app.wd
        # fill contact form
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_random_contact(0)

    def delete_random_contact(self, index):
        wd = self.app.wd
        self.open_home_page()
        # выбрать первый контакт
        wd.find_elements_by_name("selected[]")[index].click()
        # удалить выбранный контакт
        wd.find_element_by_xpath("//input[@value = 'Delete']").click()
        wd.switch_to_alert().accept()  # принять уведомление
        self.contact_cache = None

    def delete_random_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        # выбрать первый контакт
        wd.find_element_by_id(id).click()
        # удалить выбранный контакт
        wd.find_element_by_xpath("//input[@value = 'Delete']").click()
        wd.switch_to_alert().accept()  # принять уведомление
        self.contact_cache = None

    def edit(self):
        self.edit_random_contact_by_index(0)

    def edit_random_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.choose_random_contact_for_edit(index)
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                l_name = element.find_element_by_xpath("td[2]").text
                f_name = element.find_element_by_xpath("td[3]").text
                address = element.find_element_by_xpath("td[4]").text
                all_phones = element.find_element_by_xpath("td[6]").text
                all_emails = element.find_element_by_xpath("td[5]").text
                #  за исключением факса, его нет на главной странице
                self.contact_cache.append(Contact(id=id, first_name=f_name, last_name=l_name,
                                                  all_phones_from_home_page=all_phones, address=address,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        home_number = wd.find_element_by_name("home").get_attribute("value")
        mobile_number = wd.find_element_by_name("mobile").get_attribute("value")
        work_number = wd.find_element_by_name("work").get_attribute("value")
        fax_number = wd.find_element_by_name("fax").get_attribute("value")
        second_number = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(last_name=last_name, first_name=first_name, id=id, home_number=home_number,
                       mobile_number=mobile_number, work_number=work_number, fax_number=fax_number,
                       second_number=second_number, address=address, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_number = re.search("H: (.*)", text).group(1)
        mobile_number = re.search("M: (.*)", text).group(1)
        work_number = re.search("W: (.*)", text).group(1)
        fax_number = re.search("F: (.*)", text).group(1)
        return Contact(home_number=home_number, mobile_number=mobile_number, work_number=work_number,
                       fax_number=fax_number)
