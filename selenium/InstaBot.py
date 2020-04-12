import random
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from tqdm import tqdm

def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()

def login(driver, username, password):
    driver.get("https://www.instagram.com/")
    time.sleep(2)
    # login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
    # login_button.click()
    # time.sleep(2)
    user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
    user_name_elem.clear()
    user_name_elem.send_keys(username)
    passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
    passworword_elem.clear()
    passworword_elem.send_keys(password)
    passworword_elem.send_keys(Keys.RETURN)
    time.sleep(2)

def like_comments(driver, url):
    driver.get(url)
    time.sleep(2)
    # click the "Watch more comments"
    watch_count = 86
    for _ in tqdm(range(watch_count), total=watch_count):  # while True:
        try:
            btn = driver.find_element_by_xpath("//button[@class='dCJp8 afkep']")
        except NoSuchElementException as e:
            print("[OK] All comments in the screen")
            break
        btn.click()
        time.sleep(2)
    comments = driver.find_elements_by_class_name('Mr508')
    love_count, already_loved = 0, 0
    for comment in comments:
        if comment.tag_name == 'ul':
            print(f'{love_count} {already_loved}: {comment.text} \n')
            svgs = comment.find_elements_by_tag_name('svg')
            for svg in svgs:
                attr = svg.get_attribute('aria-label')
                if attr == 'Unlike':  # we haven't "loved" the button 
                    already_loved += 1
                    break
                elif attr == 'Like':  # we haven't "loved" the button 
                    try:
                        svg.click()
                    except Exception as e:
                        print("[!] IG got angry man, stop")  # ya se emputo instagram
                        return False
                    time.sleep(random.randint(1, 4))  # exec NOP randomly to avoid anti-bot algorithms
                    love_count += 1
                    break
    return True

# print (comment.text)
# print (comment.tag_name)
# print (comment.parent)
# print (comment.location)
# print (comment.size)
# print('\n\n')

driver = webdriver.Chrome('./chromedriver')
username = "__ang3lino"
password = ""
url = 'https://www.instagram.com/p/B-yNzwrlaII/'
login(driver, username, password)
success = like_comments(driver, url)
if not success:
    print(driver.page_source)
    with open('err_page.html', 'w') as f:
        f.write(driver.page_source)
time.sleep(10)
driver.close()
print('[Ok] Work done')
