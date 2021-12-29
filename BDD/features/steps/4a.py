from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@given("I'm logged into the SGME platform###")
def given(context):

    context.driver = webdriver.Chrome("")#Colocar caminho para o chromedriver.exe
    context.driver.get("")#Colocar link para a plataforma testada

    username_field = context.driver.find_element(By.ID, "login")
    username_field.send_keys("")#Inserir credencial email válido

    password_field = context.driver.find_element(By.ID, "inputPassword")
    password_field.send_keys("")#Inserir credencial senha válida

    login_button = context.driver.find_element(By.ID, "btnLogin")
    login_button.click()

@when("click on the Exit option")
def when(context):

    menu_exit = WebDriverWait(context.driver, 60).until(expected_conditions.visibility_of_element_located((
        By.XPATH, "/html/body/app-root/app-sidebar-layout/div/div/app-accessibility-bar/div/nav/div/ul/ul/li[2]/button"
    )))

    menu_exit.click()


@then("SGME platform directs me to the login page")
def then(context):
    WebDriverWait(context.driver, 60).until(expected_conditions.visibility_of_element_located((
        By.XPATH, '/html/body/app-root/app-login/div/div/app-login-form/div[1]/div/div/img'
    )))

    context.driver.quit()