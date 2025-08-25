from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests

# Replace these with the appropriate values
website_url = "https://elearning.utm.my/24251/login/index.php"  # The URL of the website
username = "chino"
password = "p*qpg3H#j*vCSKW"
username_field_id = "username"  # Replace with the 'id' or 'name' attribute of the username field
password_field_id = "password"  # Replace with the 'id' or 'name' attribute of the password field
login_button_id = "loginbtn"  # Replace with the 'id' or 'name' attribute of the login button
target_button_xpath = "//*[@id='loginbtn']"  # XPath or identifier for the button to click

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # headers = {
    #     "accept": "application/json",
    #     "content-type": "application/x-www-form-urlencoded",
    #     "x-apikey": "4e8154ee29d137f4b2c2f9916427a1542d8643afb549df1973a9e53daba58e65"
    # }

    # response = requests.post(website_url, headers=headers)
    
    # print(response.text)
    # Open the website
    driver.get(website_url)
    time.sleep(2)  # Allow the page to load

    # Enter username
    username_field = driver.find_element(By.ID, username_field_id)
    username_field.send_keys(username)

    # Enter password
    password_field = driver.find_element(By.ID, password_field_id)
    password_field.send_keys(password)

    # Click login button
    login_button = driver.find_element(By.ID, login_button_id)
    login_button.click()
    time.sleep(3)  # Allow time for login process

    # Click the target button
    target_button = driver.find_element(By.XPATH, target_button_xpath)
    target_button.click()
    print("Button clicked successfully!")

finally:
    # Close the browser
    driver.quit()
