from selenium import webdriver
import requests


PROXY = "localhost:1231" # IP:PORT or HOST:PORT
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)

driver=webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://facebook.com")

driver.find_element_by_partial_link_text("Forgotten").click()

# ele = driver.find_elements_by_tag_name("a")
# print(type(ele))
# el1=[]
# el2=[]
# for i in ele:
#     r = requests.head(i.get_attribute("href"))
#     if r.status_code !=200:
#         el1.append(i.get_attribute("href"))
#     else:
#         el2.append(i.get_attribute("href"))
# print("BL ",el1)
# print("WL ",el2)

