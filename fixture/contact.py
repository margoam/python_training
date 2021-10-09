from selenium.webdriver.support.ui import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        # добавление домашней страницы, на которой находятся созданные контакты
        wd.get("http://localhost/addressbook/index.php")

    def fill_contact_form(self, contact):
        self.edit_name_field("firstname", contact.first_name)
        self.edit_name_field("middlename", contact.middle_name)
        self.edit_name_field("nickname", contact.nickname)
        self.edit_name_field("lastname", contact.lastname)
        self.edit_name_field("home", contact.home_number)
        self.edit_name_field("mobile", contact.mobile_number)
        self.edit_name_field("mobile", contact.mobile_number)
        self.edit_name_field("mobile", contact.mobile_number)

    def edit_name_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def home_number(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_number)

    def mobile_number(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_number)

    def date_of_birth(self, contact):
        wd = self.app.wd
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.birth_day)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.birth_month)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birth_year)

    def fill_notes(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)

    def fill_second_address(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address_sec)

    def fill_email(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)

    def fill_title(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)

    def fill_company(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)

    def create(self, contact):
        wd = self.app.wd
        # fill contact form
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        self.home_number(contact)
        self.mobile_number(contact)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        self.date_of_birth(contact)
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
        # выбрать первый контакт
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        self.home_number(new_contact_data)
        self.date_of_birth(new_contact_data)
        self.fill_company(new_contact_data)
        self.fill_title(new_contact_data)
        self.fill_email(new_contact_data)
        self.fill_second_address(new_contact_data)
        self.fill_notes(new_contact_data)
        wd.find_element_by_name("update").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()
