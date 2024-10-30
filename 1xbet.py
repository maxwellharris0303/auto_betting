from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from time import sleep
import requests
import keyboard

LOGIN_ID = "716347535"
LOGIN_PWD = "e62b6ebu"

firefox_profile_directory = 'C:/Users/root/AppData/Roaming/Mozilla/Firefox/Profiles/bcgxfdql.default-release'
firefox_options = webdriver.FirefoxOptions()
firefox_options.profile = webdriver.FirefoxProfile(firefox_profile_directory)

bet_driver = webdriver.Firefox(options=firefox_options)
bet_driver.maximize_window()
bet_driver.get("https://1xbet.com/")


sleep(1000)
WebDriverWait(bet_driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"loginDropTop_con base_auth_form login-btn\"]"))).click()

id_input = WebDriverWait(bet_driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id=\"auth_id_email\"]")))
id_input.send_keys(LOGIN_ID)

pwd_input = WebDriverWait(bet_driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id=\"auth-form-password\"]")))
pwd_input.send_keys(LOGIN_PWD)

login_button = WebDriverWait(bet_driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"auth-button auth-button--block auth-button--slide-up-hover auth-button--theme-secondary\"]")))
login_button.click()

sleep(1000)