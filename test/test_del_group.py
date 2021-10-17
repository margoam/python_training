from model.group import Group
from random import randrange


def test_delete_random_group(app):  # Тестовый метод, принимающий фикстуру в качестве параметра
    if app.group.count() == 0:
        app.group.create(Group(name="test3", header="dsffsd", footer="sggsdgs"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[index:index+1] = []
    assert old_groups == new_groups

