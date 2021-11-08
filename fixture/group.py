from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_form_group(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()
        self.group_cache = None  # необходимо сбросить кеш после его модификации (невалидный)

    def fill_form_group(self, group):
        self.edit_group_field("group_name", group.name)
        self.edit_group_field("group_header", group.header)
        self.edit_group_field("group_footer", group.footer)

    def choose_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def choose_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def choose_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def edit_group_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.choose_group_by_index(index)
        # удалить случайную группу
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None  # необходимо сбросить кеш после его модификации (невалидный)

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        self.choose_group_by_id(id)
        # удалить случайную группу
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None  # необходимо сбросить кеш после его модификации (невалидный)

    def edit(self):
        self.edit_random_group_by_index(0)

    def edit_random_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.choose_group_by_index(index)
        wd.find_element_by_name("edit").click()
        self.fill_form_group(new_group_data)
        # submit group creation
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None  # необходимо сбросить кеш после его модификации (невалидный)

    def edit_random_group_by_id(self, id, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.choose_group_by_id(id)
        wd.find_element_by_name("edit").click()
        self.fill_form_group(new_group_data)
        # submit group creation
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None  # необходимо сбросить кеш после его модификации (невалидный)

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))  # модифицировать нужно именно group_cache
        return list(self.group_cache)  # возвращение копии кеша, так как снаружи он может быть испорчен
