###########################################################################
# Desctiption: Attempts to log into Facebook and if successful returns a 
#              driver object
# Name: Wesley Kerfoot, Mehdi Hachimi
# Date Created: 22/05/2019
# Date Modified: 30/05/2019
###########################################################################

import time

from selenium.webdriver.chrome.options import Options
from seleniumrequests import Chrome

def login(user_email_address, user_password, user_profile_url):
      """
      user_email_address = str Your Email
      user_password = str Your password
      user_profile_url = str Your profile URL
      """
      chrome_options = Options()
      prefs = {
            "profile.default_content_setting_values.notifications": 2, 
            'disk-cache-size': 4096
      }
      chrome_options.add_experimental_option("prefs", prefs)
      chrome_options.add_argument("start-maximized")

      driver = Chrome(options=chrome_options)
      driver.implicitly_wait(10)

      driver.get("https://facebook.com")

      email = "email"
      password = "pass"
      login = "loginbutton"

      emailelement = driver.find_element_by_name(email)
      passwordelement = driver.find_element_by_name(password)

      emailelement.send_keys(user_email_address)
      passwordelement.send_keys(user_password)

      loginelement = driver.find_element_by_id(login)
      loginelement.click()

      driver.get(user_profile_url + '/friends')
      return driver
