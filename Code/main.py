import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


tm = [int(i) for i in input("Введите время отправки в формате hh:mm:ss: ").split(":")]
receiver = input("Вставьте ссылку получателя: ")
message = input("Введите сообщение: ")


while True:
    if tm[0] == time.localtime().tm_hour and tm[1] == time.localtime().tm_min and tm[2] == time.localtime().tm_sec:
        url = [receiver,
               "/html/body/div[3]/div/div/div[2]/div[1]/div/div[1]/button[1]",
               "/html/body/div[14]/div/div/div/div[3]/div/div/div[2]/div[1]/div/div/section/div/div/div/div/div/div[2]/div/button[1]/span/span",
               "/html/body/div[14]/div/div/div/div[3]/div/div/div[2]/div[1]/div/div/section/div/div/div/div/div/form/div[1]/div[3]/span/div/div[2]/input",
               "/html/body/div[14]/div/div/div/div[3]/div/div/div[2]/div[1]/div/div/section/div/div/div/div/div/form/button[1]/span",
               "/html/body/div[1]/div/div/div/div/div[1]/div[1]/div/div/div/div/form/div[3]/button/span/span",
               "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div[4]/div[2]/div[1]/span",
               "/html/body/div[1]/div/div/div/div/div[1]/div[1]/div/div/div/div/form/div[1]/div[3]/div/div/input",
               "/html/body/div[1]/div/div/div/div/div[1]/div[1]/div/div/div/div/form/div[2]/button[1]/span",
               ]

        url_send = [
            "/html/body/div[4]/div/div/div[2]/div[2]/div[3]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/a/span",
            "/html/body/div[12]/div/div[2]/div/div[2]/div/div[4]/div[3]",
            "/html/body/div[12]/div/div[2]/div/div[2]/div/div[7]/button/span/span"]

        "//*[@id="profile_redesigned"]/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[1]/a/span/span"
        "//*[@id="profile_redesigned"]/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[1]/a/span/span"
        "//*[@id="profile_redesigned"]/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[1]/a/span/span"

        "//*[@id="profile_redesigned"]/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/a/span/span/svg"
        "//*[@id="profile_redesigned"]/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/a/span/span/svg"



        browser = webdriver.Chrome()
        browser.maximize_window()

        browser.get(url[0])

        search = browser.find_element(By.XPATH, url[1])
        search.send_keys(Keys.ENTER)

        time.sleep(5)

        search = browser.find_element(By.XPATH, url[2])
        search.click()

        time.sleep(5)

        search = browser.find_element(By.XPATH, url[3])
        search.send_keys("login")

        time.sleep(5)

        search = browser.find_element(By.XPATH, url[4])
        search.click()

        time.sleep(5)

        search = browser.find_element(By.XPATH, url[5])
        search.click()

        time.sleep(5)

        search = browser.find_element(By.XPATH, url[6])
        search.click()

        time.sleep(5)

        search = browser.find_element(By.XPATH, url[7])
        search.send_keys("password")

        time.sleep(5)

        search = browser.find_element(By.XPATH, url[8])
        search.click()

        time.sleep(5)

        browser.get(receiver)

        time.sleep(5)

        search = browser.find_element(By.XPATH, url_send[0])
        search.click()

        time.sleep(5)

        search = browser.find_element(By.XPATH, url_send[1])
        search.send_keys(message)

        time.sleep(5)

        search = browser.find_element(By.XPATH, url_send[2])
        search.click()

        time.sleep(1000)
    print(time.localtime())
    time.sleep(1)