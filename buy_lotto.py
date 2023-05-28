from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
from dotenv import load_dotenv
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

# 구매 개수를 설정
COUNT = 1


def run():
    
    load_dotenv()
    USER_ID = os.getenv('USER_ID')
    USER_PW = os.getenv('USER_PW')
    url = 'https://dhlottery.co.kr/user.do?method=login'


    chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                        # and if it doesn't exist, download it automatically,
                                        # then add chromedriver to path

    chrome_options = webdriver.ChromeOptions()    
    # Add your options as needed    
    options = [
    "--headless", # Runs Chrome in headless mode.
    "--no-sandbox", # Bypass OS security model
    "--disable-dev-shm-usage", # Overcomes limited resource problems
    "--window-size=1200,1200",
    "--ignore-certificate-errors"
    ]

    for option in options:
        chrome_options.add_argument(option)

    driver = webdriver.Chrome(options = chrome_options)

    driver.get(url)
    # time.sleep(10)  # pause for 10 seconds
    username_input = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[placeholder='아이디']")))
    username_input.click()
    username_input.send_keys(USER_ID)
    username_input.send_keys(Keys.TAB)

    password_input = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[placeholder='비밀번호']")))
    password_input.send_keys(USER_PW)
    password_input.send_keys(Keys.TAB)

    # driver.find_element(By.CSS_SELECTOR, "form[name='jform']").submit()

    # Locate the element with the name "jform" in a form and containing the text "로그인"
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//form[@name='jform']//*[contains(text(), '로그인')]"))
    )

    parent = driver.current_window_handle
    uselessWindows = driver.window_handles
    for winId in uselessWindows:
        if winId != parent: 
            driver.switch_to.window(winId)
            driver.close()
            driver.switch_to.window(parent)
            
    # Simulate pressing Enter
    element.send_keys(Keys.ENTER)
    WebDriverWait(driver, 10).until(EC.staleness_of(element))

    driver.get("https://ol.dhlottery.co.kr/olotto/game/game645.do")

    parent = driver.current_window_handle
    uselessWindows = driver.window_handles
    for winId in uselessWindows:
        if winId != parent: 
            driver.switch_to.window(winId)
            driver.close()
            driver.switch_to.window(parent)


    # Click text=자동번호발급
    # element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="자동번호발급"]')))
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'num2')))
    element.click()
    time.sleep(5)

    # # Select 1 for 구매할 개수를 선택
    select = Select(driver.find_element(By.ID, 'amoundApply'))  # replace 'select' with the actual name or id of the select tag
    select.select_by_value(str(COUNT))
    time.sleep(5)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btnSelectNum"))).click()

    # # Click input:has-text("구매하기")
    # element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[contains(text(),"구매하기")]')))
    # element.click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btnBuy"))).click()
    time.sleep(2)

    #clicking 확인 button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="popupLayerConfirm"]/div/div[2]/input[1]'))).click()


    # # Click input[name="closeLayer"]
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'closeLayer')))
    element.click()

    # # assert page.url == "https://el.dhlottery.co.kr/game/TotalGame.jsp?LottoId=LO40"
    # assert driver.current_url == "https://el.dhlottery.co.kr/game/TotalGame.jsp?LottoId=LO40"
    time.sleep(10)

    driver.close()
    driver.quit()

run()

