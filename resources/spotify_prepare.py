from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SpotifyPrepare:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def connect():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://open.spotify.com/')

        return driver

    def login(self, driver):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'KQWHP'))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'login-username')))

        username_input = driver.find_element(By.ID, 'login-username')
        password_input = driver.find_element(By.ID, 'login-password')
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'login-button'))).click()

        return

    @staticmethod
    def accept_cookies(driver):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))).click()

        return
