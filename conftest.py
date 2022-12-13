import allure
import pytest
from _pytest.fixtures import FixtureRequest
from utils.base_user import BaseSession


@pytest.fixture(scope='session')
def reqres_session():
    with BaseSession(base_url='https://reqres.in') as session:
        yield session


