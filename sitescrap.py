from selenium import webdriver
import time,os


def send_data(details):
    if len(details)>=2:

        path = "user-data-dir=C:\\Users\\ksh09\\AppData\\Local\\Google\\Chrome\\User Data\\Whatsapp"  # path where session info you want to store
        options = webdriver.ChromeOptions()
        options.add_argument(path)

        driver = webdriver.Chrome("C://Webdriver//chromedriver.exe", options=options)

        driver.get("http://136.232.2.202:8084/resstude20.aspx")

        time.sleep(1)
        roll=driver.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/input')
        roll.send_keys(details[0])
        sem=driver.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/select')
        sem.send_keys(details[1])
        show=driver.find_element_by_xpath('//*[@id="Button1"]')
        show.click()
        driver.execute_script("document.body.style.zoom='80%'")
        driver.find_element_by_xpath('//*[@id="form1"]/table/tbody').screenshot("img/{}.png".format(details[0]))
        driver.close()




