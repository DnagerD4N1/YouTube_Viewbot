from selenium import webdriver
from time import sleep

driver1 = webdriver.Chrome(executable_path="/Users/danny/Desktop/YouTube_ViewBot/chromedriver")
driver2 = webdriver.Chrome(executable_path="/Users/danny/Desktop/YouTube_ViewBot/chromedriver")
driver3 = webdriver.Chrome(executable_path="/Users/danny/Desktop/YouTube_ViewBot/chromedriver")

driver1.get("https://www.youtube.com/watch?v=X0c06JzDzjI&feature=youtu.be")
driver2.get("https://www.youtube.com/watch?v=X0c06JzDzjI&feature=youtu.be")
driver3.get("https://www.youtube.com/watch?v=X0c06JzDzjI&feature=youtu.be")

while True:
    sleep(181.2)
    driver1.refresh()
    driver2.refresh()
    driver3.refresh()
