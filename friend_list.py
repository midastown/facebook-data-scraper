###########################################################################
# Desctiption: Retrieves Current City data if it is available in each 
#              friends page otherwise it will issue a "not specified".
#              If photo link is dead, it will issue a "No Active Account"
# Name: Mehdi Hachimi
# Date Created: 26/05/2019
# Date Modified: 30/05/2019
###########################################################################

import time
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

SELENIUM_EXCEPTIONS = (NoSuchElementException, ElementClickInterceptedException)


MAX_FRIENDS = 5000

def retrieve_location_from_friends(driver):
    """
    driver = obj Chrome driver
    returns a list of locations
    """
    data = []
    element_li = '_698'
    counter = 0
    script = "window.scrollTo(0, document.body.scrollHeight);"

    # Scrolling down
    for index in range(0, MAX_FRIENDS):
        if (index % 15) == 0 and index != 0:
            counter += 1
            for i in range(counter):
                driver.execute_script(script)
                time.sleep(3)
        elif counter >= 1:
            for i in range(counter):
                driver.execute_script(script)
                time.sleep(3)
         
        # reloading list elements -> no Slate element exception 
        friend_list_elements = driver.find_elements_by_class_name(element_li)

        if index >= len(friend_list_elements):
            break
      
      
        try:
           photo_link = friend_list_elements[index].find_element_by_xpath(".//a[contains(@class, '_5q6s')]")
        except SELENIUM_EXCEPTIONS:
           data.append("No Active Account")
           continue
      
        photo_link.click()

        try:
           location = driver.find_element_by_xpath(".//a[contains(@href, 'current_city&timeline')]")
        except SELENIUM_EXCEPTIONS:
           location = "not specified"
           data.append(location)
           driver.back()
           time.sleep(2)
           continue
     
        time.sleep(1)
        data.append(location.text)
        driver.back()
        time.sleep(2)

    return data
