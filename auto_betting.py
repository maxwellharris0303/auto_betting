from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from time import sleep
import requests
import keyboard

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.whoscored.com")

WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\" css-1wc0q5e\"]"))).click()

WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class=\"Match-module_previewBtn__mYHIm\"]")))

preview_buttons = driver.find_elements(By.CSS_SELECTOR, "a[class=\"Match-module_previewBtn__mYHIm\"]")
print(len(preview_buttons))
match_links = []
for preview_button in preview_buttons:
    # print(preview_button.get_attribute('href'))
    match_links.append(preview_button.get_attribute('href'))

print(match_links)
driver.quit()

match_driver = webdriver.Chrome()
match_driver.maximize_window()
match_driver.get(match_links[0])
WebDriverWait(match_driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\" css-1wc0q5e\"]"))).click()

team_names_array = []
predict_scores_array = []
for url in match_links:
    match_driver.get(url)
    prediction_parent_element = WebDriverWait(match_driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id=\"preview-prediction\"]")))
    team_links = prediction_parent_element.find_elements(By.CSS_SELECTOR, "a[class=\"team-link\"]")
    predict_scores = prediction_parent_element.find_elements(By.CSS_SELECTOR, "span[class=\"predicted-score\"]")
    for team_link in team_links:
        team_name = team_link.find_element(By.CSS_SELECTOR, ":first-child").text
        # print(team_name)
        team_names_array.append(team_name)
    for predict_score in predict_scores:
        predict_score = predict_score.text
        # print(predict_score)
        predict_scores_array.append(predict_score)

print(team_names_array)
print(predict_scores_array)
match_driver.quit()

LOGIN_ID = "716347535"
LOGIN_PWD = "e62b6ebu"

firefox_profile_directory = 'C:/Users/root/AppData/Roaming/Mozilla/Firefox/Profiles/bcgxfdql.default-release'
firefox_options = webdriver.FirefoxOptions()
firefox_options.profile = webdriver.FirefoxProfile(firefox_profile_directory)

bet_driver = webdriver.Firefox(options=firefox_options)
bet_driver.maximize_window()
bet_driver.get("https://1xbet.com/")


sleep(1000)
sleep(1000)