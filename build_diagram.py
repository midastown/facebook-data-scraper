###########################################################################
# Desctiption: Parse data to comply with syntax, builds diagram using
#              sankeymatic.com and downloads its png
# Name: Mehdi Hachimi
# Date Created: 26/05/2019
# Date Modified: 30/05/2019
###########################################################################


import time 
from seleniumrequests import Chrome


def build_diagram(data):
    first_level = {'Active Profiles': 0}
    second_level = {}
    data_dict = data_to_dictionary(data)
    print(data_dict)
    for single_data in data_dict:
        if single_data == "No Active Account":
            first_level['Inactive Profiles'] = data_dict[single_data]
        else:
            first_level['Active Profiles'] += data_dict[single_data]
            second_level[single_data] = data_dict[single_data]

    syntax_string = ''

    for value in first_level:
        syntax_string += value + '[' + str(first_level[value]) + '] Friends\n' 
    for value in second_level:
        syntax_string += 'Friends [' + str(second_level[value]) + '] ' + value + '\n'

    driver = Chrome()
    driver.get('http://sankeymatic.com/build')

    input_element = driver.find_element_by_xpath('//*[@id="flows_in"]')
    input_element.clear()
    input_element.send_keys(syntax_string)

    preview_button = driver.find_element_by_xpath('//*[@id="preview_graph"]')
    preview_button.click()

    png_img = driver.find_element_by_xpath('//*[@id="export_options"]/h3[1]/abbr')
    png_img.click()

    download_diagram = driver.find_element_by_xpath('//*[@id="download_png_link"]')
    download_diagram.click()
    time.sleep(10)

def data_to_dictionary(data):
    data_dict = {}
    for entry in data:
        if entry in data_dict:
            data_dict[entry] += 1
        else:
            data_dict[entry] = 1
    return data_dict
