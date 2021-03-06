from model.group import Group
import random


def test_delete_random_group(app, db, check_ui):  # Тестовый метод, принимающий фикстуру в качестве параметра
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test3", header="dsffsd", footer="sggsdgs"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
