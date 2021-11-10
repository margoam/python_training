from model.group import Group
import random


def test_edit_group(app, db, check_ui):  # Тестовый метод, принимающий фикстуру в качестве параметра
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test4", header="header_test", footer="footer_test"))
    old_groups = db.get_group_list()
    group = Group(name="edit_test3")
    groups = random.choice(old_groups)
    old_groups.remove(groups)
    group.id = groups.id
    app.group.edit_random_group_by_id(groups.id, group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
