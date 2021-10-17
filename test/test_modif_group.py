from model.group import Group


def test_edit_group(app):  # Тестовый метод, принимающий фикстуру в качестве параметра
    if app.group.count() == 0:
        app.group.create(Group(name="test4", header="header_test", footer="footer_test"))
    old_groups = app.group.get_group_list()
    group = Group(name="edit_test3")
    group.id = old_groups[0].id
    app.group.edit(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
