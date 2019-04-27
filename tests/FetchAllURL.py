from selenium import webdriver
import requests

driver=webdriver.Chrome()
driver.get("http://google.com")
element = driver.find_elements_by_tag_name("a")
print(type(element))#list
print(len(element))#50

broken_link=[]
correct_link=[]
for i in element:
    if(requests.head(i.get_attribute("href")) !=200):
        broken_link.append(i.get_attribute("href"))
    else:
        correct_link.append(i.get_attribute("href"))
print("broken_link list ",broken_link)
print("working link list ",correct_link)
