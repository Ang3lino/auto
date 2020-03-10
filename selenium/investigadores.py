
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import selenium

import requests
from bs4 import BeautifulSoup
# from tqdm import tqdm 
import time


def update_drivers():
    global sel_insti, sel_area, sel_edo, button
    sel_insti = Select(driver.find_element_by_id('id_insti'))
    sel_area = Select(driver.find_element_by_id('id_area'))
    sel_edo = Select(driver.find_element_by_id('id_edo'))
    button = driver.find_element_by_class_name('inputboton')

def get_values(soup, id_select: str):
    soup_object = soup.find(id=id_select)
    groups = soup_object.find_all('optgroup')
    values = []
    for grp in (groups):
        values.append([x['value'] for x in grp.find_all('option')])
    return values

def find_researchers(institutions, locations, fname):
    progress, total = 0, len(institutions)*len(locations)
    for institution in institutions:
        for location in locations:
            try:
                sel_insti.select_by_value(institution)
                sel_area.select_by_value('00007')
                sel_edo.select_by_value(location)
            except selenium.common.exceptions.NoSuchElementException:
                print('Exception ==> ', institutions, locations)
                continue 
            button.click()
            src = driver.page_source
            soup = BeautifulSoup(src, 'lxml')

            table = soup.find(id='tabla')
            progress += 1
            print(f'{progress} / {total}')
            if table is not None:
                msg = f'Institucion: {institution}\nUbicacion: {location}\n{str(table)}\n\n' 
                print(msg)
                with open(f'{fname}.html', 'a') as f:
                    f.write(msg)

            update_drivers()

def Soup():
    result = requests.get(url)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    return soup


# soup object
url = 'http://www.programadelfin.org.mx/usuarios/inicio-catalogoinvestigadores-ver.php#encontrados'
soup = Soup()

institution_groups = get_values(soup, 'id_insti')
location_groups = get_values(soup, 'id_edo')

i = 0
institutions = institution_groups[i]
locations = location_groups[i]

driver = webdriver.Chrome('./chromedriver')
driver.get(url)
update_drivers()

fnames = ['mexico', 'canada', 'colombia', 'costaRica', 'espana', 'estadosUnidos', \
        'nicaragua', 'peru', 'uruguay', 'venezuela']
for i in range(2, len(fnames)):
    print(fnames[i].upper(), '\n')
    find_researchers(institutions[i], locations[i], fnames[i])

time.sleep(4)
driver.close()


# sel_insti.select_by_value('00774')
# sel_area.select_by_value('00007')
# sel_edo.select_by_value('00078')

