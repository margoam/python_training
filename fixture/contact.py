from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("results")) > 0):
            wd.get("http://localhost/addressbook/index.php")

    def fill_contact_form(self, contact):
        self.edit_name_field("firstname", contact.first_name)
        self.edit_name_field("middlename", contact.middle_name)
        self.edit_name_field("nickname", contact.nickname)
        self.edit_name_field("lastname", contact.last_name)
        self.edit_name_field("home", contact.home_number)
        self.edit_name_field("byear", contact.birth_year)
        self.edit_name_field("mobile", contact.mobile_number)
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
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def create(self, contact):
        wd = self.app.wd
        # fill contact form
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        # выбрать первый контакт
        wd.find_element_by_name("selected[]").click()
        # удалить выбранный контакт
        wd.find_element_by_xpath("//input[@value = 'Delete']").click()
        wd.switch_to_alert().accept()  # принять уведомление

    def edit(self, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.choose_first_contact_for_edit()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_home_page()
        contacts = []
        for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
            id = element.find_element_by_name("selected[]").get_attribute("value")
            l_name = element.find_element_by_xpath("td[2]").text
            f_name = element.find_element_by_xpath("td[3]").text
            contacts.append(Contact(id=id, first_name=f_name, last_name=l_name))
        return contacts
