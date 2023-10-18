from selenium import webdriver
from src.pages.homepage import Homepage
from src.pages.sign_up_page import SignInPage


def test_browserstack():
    driver = webdriver.Firefox()
    driver.get("https://bstackdemo.com/")

    homepage = Homepage(driver)
    sign_in_page = SignInPage(driver)

    homepage.click_sign_in()

    sign_in_page.select_username()
    sign_in_page.select_password()
    sign_in_page.click_login()
    homepage.get_username()
    driver.quit()
