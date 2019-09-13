###########################################################################
# Desctiption: Scour the facebook website, retrieve data and build diagram 
#              out of it
# Name: Mehdi Hachimi
# Date Created: 26/05/2019
# Date Modified: 30/05/2019
###########################################################################

from login import login
from friend_list import retrieve_location_from_friends
from getpass import getpass
from build_diagram import build_diagram


URL = 'https://www.facebook.com/'
username = input('Please write your username of type https://www.facebook.com/USERNAME : ')
email = input('Please write you mailing address : ')
password = getpass()
URL_profile = URL + username


if __name__ == "__main__":
    # Logs into account and return a Chrome Driver Object
    driver = login(email, password, URL_profile)
    # Scour your friends list and returns a list with apropriate data
    data = retrieve_location_from_friends(driver)
    # Builds intuitive diagram using the popular website http://sankeymatic.com
    build_diagram(data)
