import json
import pytest
import os.path
import importlib
from fixture.application import Application

fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:  # f - содержит объект, указывающий на открытый файл
            target = json.load(f)
    username = request.config.getoption("--username")
    password = request.config.getoption("--password")
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target['baseUrl'], username=target['username'],
                              password=target['password'])  # Инициализация фикстуры
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
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--username", action="store", default="target.json")
    parser.addoption("--password", action="store", default="target.json")


def pytest_generate_tests(metafunc):  # генерация тестов
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata
