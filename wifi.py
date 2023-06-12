from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')

# Specify the path to the ChromeDriver executable or left blank if already added in PATH variable
# driver_path = 'C:/Users/Keshav/Desktop/chromedriver_win32/chromedriver.exe'

driver = webdriver.Chrome(options=options)


def login(username, password):
    driver.get('https://172.22.2.6/connect/PortalMain')
    wait = WebDriverWait(driver, 4)

    # Wait for the username field to be present
    username_field = wait.until(EC.presence_of_element_located(
        (By.ID, 'LoginUserPassword_auth_username')))
    username_field.send_keys(username)

    # Wait for the password field to be present
    password_field = wait.until(EC.presence_of_element_located(
        (By.ID, 'LoginUserPassword_auth_password')))
    password_field.send_keys(password)

    # Submit the login form
    login_button = wait.until(EC.element_to_be_clickable(
        (By.ID, 'UserCheck_Login_Button')))
    login_button.click()


login('20uec068', 'password')  # Replace with your username and password

while True:
    login('20uec068', 'password')  # Replace with your username and password
    time.sleep(3 * 60 * 60)  # Sleep for 3 hours
# although the duration of one login session is for 4 hours, the script is set to login every 3 hours to avoid any issues
