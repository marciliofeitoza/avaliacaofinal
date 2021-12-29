from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@given("a user is in the SGME platform login page#")
def given(context):
    pass
    context.driver = webdriver.Chrome("")#Colocar caminho para o chromedriver.exe
    context.driver.get("")#Colocar link para a plataforma testada

@when("the user insert his invalid credentials")
def when(context):
    username_field = context.driver.find_element_by_id("login")
    username_field.send_keys("")#Inserir credencial inválido

    password_field = context.driver.find_element_by_id("inputPassword")
    password_field.send_keys("")#Inserir credencial inválido

    login_button = context.driver.find_element_by_id("btnLogin")
    login_button.click()


@then("SGME plataform returns that the credentials are not valid")
def then(context):
    WebDriverWait(context.driver, 60).until(expected_conditions.visibility_of_element_located((
        By.XPATH, '/html/body/app-root/app-login/div/div/app-login-form/div[2]/div/div/div/form/div[1]'
    )))