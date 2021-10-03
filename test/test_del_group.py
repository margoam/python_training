
def test_delete_first_group(app):  # Тестовый метод, принимающий фикстуру в качестве параметра
    app.session.login(username="admin", password="secret")  # всп метод
    app.group.delete_first_group()
    app.session.logout()  # всп метод