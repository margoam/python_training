from model.group import Group


def test_edit_group(app):  # Тестовый метод, принимающий фикстуру в качестве параметра
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="test4", header="header_test", footer="footer_test"))
    app.group.edit(Group(name="edit_test3"))  # всп метод
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
