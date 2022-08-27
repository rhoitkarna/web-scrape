from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url = "https://annapurnapost.com/"
driver = webdriver.Chrome(executable_path="./chromedriver")
driver.get(url)

search_text = "खेलकुद"

search_key = driver.find_element(By.CLASS_NAME, 'search-icon')
search_key.click()
sleep(1)

search_input = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div/header/div[2]/div[2]/input')
search_input.send_keys(search_text)

search_icon = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/header/div[2]/div[2]/div")
search_icon.click()
sleep(2)

print('Please wait while the script fetches the articles.')
article_list = []
for i in range(1, 35):
    article = driver.find_element(By.XPATH, f'//*[@id="searchPage"]/div/div[2]/div[{i}]/div/li/div[2]/div/h3/a').text
    article_list.append(article)
    if i % 5 == 0:
        print('Please Wait...')
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)

article_dict = {}
for index, value in enumerate(article_list):
    article_dict[index] = value

print('Here are the top articles of the day according to your search')
print(article_dict)