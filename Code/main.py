import time
from selenium import webdriver
from selenium.webdriver.common.by import By


dt = [int(i) for i in input("Введите дату отправки в формате mm:dd ").split(":")]
tm = [int(i) for i in input("Введите время отправки в формате hh:mm:ss: ").split(":")]
receivers = input("Вставьте ссылки получателей через запятую без пробелов: ").split(",")
message = input("Введите сообщение: ")

while True:
    if (tm[0] == time.localtime().tm_hour and tm[1] == time.localtime().tm_min and tm[2] == time.localtime().tm_sec\
            and dt[0] == time.localtime().tm_mon and dt[1] == time.localtime().tm_mday):
        urls = ["https://vk.com/?to=c3RpbGxtb3J0YWw-",
               "/html/body/div[14]/div/div/div/div[3]/div/div/div[2]/div[1]/div/div/section/div/div/div/div/div/div[2]/div/button[1]/span/span",
               "/html/body/div[14]/div/div/div/div[3]/div/div/div[2]/div[1]/div/div/section/div/div/div/div/div/form/div[1]/div[3]/span/div/div[2]/input",
               "/html/body/div[14]/div/div/div/div[3]/div/div/div[2]/div[1]/div/div/section/div/div/div/div/div/form/button[1]/span",
               "/html/body/div[1]/div/div/div/div/div[1]/div[1]/div/div/div/div/form/div[3]/button/span/span",
               "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div[4]/div[2]/div[1]/span",
               "/html/body/div[1]/div/div/div/div/div[1]/div[1]/div/div/div/div/form/div[1]/div[3]/div/div/input",
               "/html/body/div[1]/div/div/div/div/div[1]/div[1]/div/div/div/div/form/div[2]/button[1]/span",
               ]

        urls_send = ["//*[@id='mail_box_editable']",
                    "//*[@id='mail_box_send']/span/span"]

        friend = "//*[@id='profile_redesigned']/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[1]/a/span/span"
        not_friend = "#profile_redesigned > div > div > div > div.ProfileHeader.ProfileHeader--withSnowballs > div.ProfileHeader__in > div.ProfileHeader__wrapper > div > div.ProfileHeader__actions > div > div > div > div:nth-child(2) > a > span > span > svg"

        # entrance
        browser = webdriver.Chrome()
        browser.maximize_window()

        browser.get(urls[0])

        time.sleep(5)

        search = browser.find_element(By.XPATH, urls[1])
        search.click()

        time.sleep(5)

        search = browser.find_element(By.XPATH, urls[2])
        search.send_keys("login")

        time.sleep(5)

        search = browser.find_element(By.XPATH, urls[3])
        search.click()

        time.sleep(5)

        search = browser.find_element(By.XPATH, urls[4])
        search.click()

        time.sleep(5)

        search = browser.find_element(By.XPATH, urls[5])
        search.click()

        time.sleep(5)

        search = browser.find_element(By.XPATH, urls[6])
        search.send_keys("password")

        time.sleep(5)

        search = browser.find_element(By.XPATH, urls[7])
        search.click()

        time.sleep(5)

        # sending
        for receiver in receivers:
            browser.get(receiver)

            time.sleep(5)

            try:
                search = browser.find_element(By.CSS_SELECTOR, not_friend)
                search.click()
            except Exception:
                search = browser.find_element(By.XPATH, friend)
                search.click()

            time.sleep(5)

            search = browser.find_element(By.XPATH, urls_send[0])
            search.send_keys(message)

            time.sleep(5)

            search = browser.find_element(By.XPATH, urls_send[1])
            search.click()
    print(time.localtime())
    time.sleep(1)
