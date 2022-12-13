import allure
from allure_commons.types import Severity
from requests import Response
from tests.shema.shema import *
from pytest_voluptuous import S


@allure.epic('Test API')
@allure.feature('POST запрос')
@allure.severity(Severity.CRITICAL)
@allure.step('Запрос для создания пользователя')
def test_create_user(reqres_session, lambda_steps):
    name = 'Margo'
    job = 'Doctor'

    result: Response = reqres_session.post(url='/api/users',
                                           json={"name": name, "job": job})

    assert result.status_code == 201
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert isinstance(result.json()['id'], str)
    assert result.json() == S(create_user)


@allure.epic('Test API')
@allure.feature('PUT запрос')
@allure.severity(Severity.MINOR)
@allure.step('Запрос для обновления информации о пользователе')
def test_update_user(reqres_session):
    name = 'Margo'
    job = 'QA'

    result: Response = reqres_session.put(url='/api/users/2',
                                          json={"name": name, "job": job})

    assert result.status_code == 200
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert result.json() == S(update_user)


@allure.epic('Test API')
@allure.feature('GET запрос')
@allure.severity(Severity.MINOR)
@allure.step('Пользователь не найден')
def test_user_not_found(reqres_session, lambda_steps):
    result: Response = reqres_session.get(url='/api/unknown/23')

    assert result.status_code == 404
    assert result.json() == S(user_not_found)


@allure.epic('Test API')
@allure.feature('DELETE запрос')
@allure.severity(Severity.CRITICAL)
@allure.step('Запрос для удаления пользователя')
def test_delete_user(reqres_session,lambda_steps):
    result = reqres_session.delete(url='/api/users/2')

    assert result.status_code == 204


@allure.epic('Test API')
@allure.feature('POST запрос')
@allure.severity(Severity.CRITICAL)
@allure.step('Пользователь не зарегистрирован')
def test_register_unsuccessful(reqres_session):
    email = 'peter@klaven'

    result: Response = reqres_session.post(url='/api/login',
                                           json={"email": email})

    assert result.status_code == 400
    assert result.json() == S(register_unsuccessful)