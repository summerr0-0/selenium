import time

import pyautogui
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def print_hi():
    # 셀레니움 옵션
    option = Options()
    service = Service()
    driver = webdriver.Chrome(service=service, options=option)

    # 페이지 이동
    driver.get("")
    driver.get("")
    # 브라우저 정보
    print("driver.title : ", driver.title)

    # 요소 찾기
    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    # 대기
    driver.implicitly_wait(3)

    # 대기전략(실패)
    WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(By.ID, "message"))

    # 요소에 대한 조치
    text_box.send_keys("Selenium")
    sleep(2)
    submit_button.click()

    # 대기전략(성공)
    WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(By.ID, "message"))

    # element 정보 요청
    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    pyautogui.alert(text='', title='', button='OK')

    # 세션 종료
    driver.quit()


if __name__ == '__main__':
    print_hi()
