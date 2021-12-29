from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@given("I'm logged into the SGME platform")
def given(context):

    context.driver = webdriver.Chrome("")#Colocar caminho para o chromedriver.exe
    context.driver.get("")#Colocar link para a plataforma testada

    username_field = context.driver.find_element(By.ID, "login")
    username_field.send_keys("")#Inserir credencial email válido

    password_field = context.driver.find_element(By.ID, "inputPassword")
    password_field.send_keys("")#Inserir credencial senha válida

    login_button = context.driver.find_element(By.ID, "btnLogin")
    login_button.click()

@when("click on the users menu")
def when(context):

    menu_users = WebDriverWait(context.driver, 60).until(expected_conditions.visibility_of_element_located((
        By.XPATH, "/html/body/app-root/app-sidebar-layout/div/nav/div/div[2]/ul[1]/li[3]/a"
    )))

    menu_users.click()


@then("SGME platform directs me to the users")
def then(context):
    WebDriverWait(context.driver, 200).until(expected_conditions.visibility_of_element_located((
        By.XPATH, '/html/body/app-root/app-sidebar-layout/div/div/app-administrator/div/app-users/div/div/app-custom-card/div/div[1]/span[1]/span'
    )))

    context.driver.quit()