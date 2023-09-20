import time

import pyautogui
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


def print_hi():
    # 셀레니움 옵션
    option = Options()
    service = Service()
    driver = webdriver.Chrome(service=service, options=option)

    # 페이지 이동
    driver.get("")
    # 브라우저 정보
    print("driver.title : ", driver.title)

    # 요소 찾기
    id_box = driver.find_element(by=By.XPATH, value="/html/body/div/div/form/div[1]/div/div/span/span/input")
    password_box = driver.find_element(by=By.XPATH, value="/html/body/div/div/form/div[2]/div/div/span/span/input")
    phone_box = driver.find_element(by=By.XPATH, value="/html/body/div/div/form/div[3]/div/div/span/span/input")
    submit_button = driver.find_element(by=By.XPATH, value="/html/body/div/div/form/div[3]/div/div/span/button")
    login_button = driver.find_element(by=By.XPATH, value="/html/body/div/div/form/div[5]/div/div/span/button")
    # driver.find_element(By.XPATH, '//button[text()="Some text"]')
    # driver.find_element(By.XPATH, '//button')
    # driver.find_element(By.ID, 'loginForm')
    # driver.find_element(By.LINK_TEXT, 'Continue')
    # driver.find_element(By.PARTIAL_LINK_TEXT, 'Conti')
    # driver.find_element(By.NAME, 'username')
    # driver.find_element(By.TAG_NAME, 'h1')
    # driver.find_element(By.CLASS_NAME, 'content')
    # driver.find_element(By.CSS_SELECTOR, 'p.content'


    # 대기전략(실패)
    # WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(By.ID, "message"))

    # 요소에 대한 조치
    id_box.send_keys("")
    password_box.send_keys("")
    phone_box.send_keys("")
    time.sleep(1)
    submit_button.click()
    time.sleep(3)

    # 대기
    certification_number_box = driver.find_element(by=By.XPATH, value="/html/body/div/div/form/div[4]/div/div/span/span/input")
    certification_number_box.send_keys("")

    time.sleep(3)
    login_button.send_keys(Keys.ENTER)

    # # 대기

    driver.implicitly_wait(60)



    # element 정보 요청
    # message = driver.find_element(by=By.ID, value="message")
    # value = message.text
    # pyautogui.alert(text='', title='', button='OK')



    # 세션 종료
    driver.quit()


if __name__ == '__main__':
    print_hi()
