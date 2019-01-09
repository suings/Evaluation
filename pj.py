import os
import re
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()

if os.path.exists("/usr/bin/chromedriver"):
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    browser = webdriver.Chrome(options=chrome_options)
else:
    browser = webdriver.Chrome(options=chrome_options,
                               executable_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe", )

wait = WebDriverWait(browser, 5)


def pj(u, pwd, sleep_time=0.5):
    browser.delete_all_cookies()
    browser.get("http://221.233.24.23/eams/login.action")

    browser.find_element_by_id("username").send_keys(u)
    browser.find_element_by_id("password").send_keys(pwd)
    time.sleep(sleep_time)
    browser.find_element_by_name("submitBtn").click()

    while True:
        pagesource = browser.page_source

        if "请不要过快点击" in pagesource:
            sleep_time += 1
            return pj(u, pwd, sleep_time)

        if "忘记密码" in pagesource:
            if "密码错误" in pagesource or "账户不存在" in pagesource:
                return "pwd err"
        elif "我的账户" in pagesource:
            break

    browser.get("http://221.233.24.23/eams/quality/stdEvaluate.action")
    regex = re.compile("/eams/quality/stdEvaluate![^\"]*")
    for link in regex.findall(pagesource):
        link = "http://221.233.24.23" + link
        browser.get(link)
        [option.send_keys(Keys.SPACE) for option in
         wait.until(EC.presence_of_all_elements_located((By.XPATH, '//input[@value="0"]')))]
        browser.find_element_by_id("sub").click()
        browser.switch_to.alert.accept()
    return "success"
