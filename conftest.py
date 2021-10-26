import pytest
from fixture.application import Application

fixture = None


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    username = request.config.getoption("--username")
    password = request.config.getoption("--password")
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url, username=username, password=password)  # Инициализация фикстуры
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_url=base_url, username=username, password=password)  # Инициализация фикстуры
    fixture.session.ensure_login(username, password)
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)  # Как должна быть разрушена фикстура
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/index.php")
    parser.addoption("--username", action="store")
    parser.addoption("--password", action="store")
