from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.wait as wait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, NoSuchWindowException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from dotenv import load_dotenv
import os
import sys

import time
import undetected_chromedriver as uc
import re
def trade_size(TRADE_SIZE):
    #//*[@id="inputs"]

    
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='inputs']")))
    inputs=driver.find_element(by=By.XPATH, value="//*[@id='inputs']")
    inputs.click()
    #//*[@id="overlap-manager-root"]/div/div/div[1]/div/div[3]/div/div[18]/div/span/span[1]/input
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='overlap-manager-root']/div/div/div[1]/div/div[3]/div/div[18]/div/span/span[1]/input")))
    trade_size=driver.find_element(by=By.XPATH, value="//*[@id='overlap-manager-root']/div/div/div[1]/div/div[3]/div/div[18]/div/span/span[1]/input")
    trade_size_previous=trade_size.get_attribute("value")
    num_of_backspaces = len(trade_size_previous)

    for _ in range(num_of_backspaces):
        trade_size.send_keys(Keys.BACKSPACE)
    
    trade_size.send_keys(TRADE_SIZE)
    print("Successfully sent trade size")
    print(f"Trade size: {trade_size.text}")

def initial_amount(INITIAL_AMOUNT):
    #//*[@id="properties"]
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='properties']")))
    properties=driver.find_element(by=By.XPATH, value="//*[@id='properties']")
    properties.click()
    #//*[@id="overlap-manager-root"]/div/div/div[1]/div/div[3]/div/div[2]/div/span/span[1]/input
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='overlap-manager-root']/div/div/div[1]/div/div[3]/div/div[2]/div/span/span[1]/input")))
    initial_amount=driver.find_element(by=By.XPATH, value="//*[@id='overlap-manager-root']/div/div/div[1]/div/div[3]/div/div[2]/div/span/span[1]/input")
    initial_amount_previous=initial_amount.get_attribute("value")
    num_of_backspaces = len(initial_amount_previous)

    for _ in range(num_of_backspaces):
        initial_amount.send_keys(Keys.BACKSPACE)
    
    initial_amount.send_keys(INITIAL_AMOUNT)
    print("Successfully sent initial amount")
    print(f"Initial amount: {initial_amount.text}")
    
    
    

def main(TICKER, TIMEFRAME_RANGE, INITIAL_AMOUNT, TRADE_SIZE, DEBUG):
    Username= user
    Password= pswrd
    #Testing a trading strategy by going thru different timeframes to see which yields the best results

    #Set up the driver
    driver.get("https://www.tradingview.com")

    #/html/body/div[3]/div[3]/div[2]/div[3]/button[1]/svg/path

    time.sleep(4)
    try:
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div[2]/div[3]/button[1]")))
        Signin=driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[3]/div[2]/div[3]/button[1]")
        Signin.click()
        print("clicked")
        #//*[@id="overlap-manager-root"]/div/span/div[1]/div/div/div/button[1]/span/span/span/span[2]/span[1]
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='overlap-manager-root']/div/span/div[1]/div/div/div/button[1]/span/span/span/span[2]/span[1]")))
        Signinsecond=driver.find_element(by=By.XPATH, value="//*[@id='overlap-manager-root']/div/span/div[1]/div/div/div/button[1]/span/span/span/span[2]/span[1]")
        Signinsecond.click()
        print("clicked")
        #/html/body/div[9]/div/div/div[1]/div/div[2]/div[2]/div/div/button
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[9]/div/div/div[1]/div/div[2]/div[2]/div/div/button")))
        Signinthird=driver.find_element(by=By.XPATH, value="/html/body/div[9]/div/div/div[1]/div/div[2]/div[2]/div/div/button")
        Signinthird.click()
        #//*[@id="id_username"]
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='id_username']")))
        username=driver.find_element(by=By.XPATH, value="//*[@id='id_username']")
        username.send_keys(Username)
        #//*[@id="id_password"]
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='id_password']")))
        password=driver.find_element(by=By.XPATH, value="//*[@id='id_password']")
        password.send_keys(Password)
        
        #/html/body/div[9]/div/div/div[1]/div/div[2]/div[2]/div/div/div/form/button
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[9]/div/div/div[1]/div/div[2]/div[2]/div/div/div/form/button")))
        login=driver.find_element(by=By.XPATH, value="/html/body/div[9]/div/div/div[1]/div/div[2]/div[2]/div/div/div/form/button")
        login.click()
        time.sleep(5)
        #//*[@id="recaptcha-anchor-label"]

        login_successful=False

        while not login_successful:
            try:
                WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[9]/div/div/div[1]/div/div[2]/div[2]/div/div/div/form/button")))
                login=driver.find_element(by=By.XPATH, value="/html/body/div[9]/div/div/div[1]/div/div[2]/div[2]/div/div/div/form/button")
                login.click()
                time.sleep(5)
                login_successful = True
            except (NoSuchElementException, ElementClickInterceptedException):
                print("Login failed, retrying...")
                time.sleep(2)  # wait for 2 seconds before retrying
    
        WebDriverWait(driver,20).until(EC.url_changes("https://www.tradingview.com/"))
        #/html/body/div[4]/div[3]/div[2]/div[1]/button
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[3]/div[2]/div[1]/button")))
        burger=driver.find_element(by=By.XPATH, value="/html/body/div[4]/div[3]/div[2]/div[1]/button")
        burger.click()
        #//*[@id="overlap-manager-root"]/div[2]/span/div[1]/div/div/div/div/button[1]
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='overlap-manager-root']/div[2]/span/div[1]/div/div/div/div/button[1]")))
        products=driver.find_element(by=By.XPATH, value="//*[@id='overlap-manager-root']/div[2]/span/div[1]/div/div/div/div/button[1]")
        products.click()
        #//*[@id="overlap-manager-root"]/div[2]/span/div[1]/div/div/div[3]/div/a[1]
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='overlap-manager-root']/div[2]/span/div[1]/div/div/div[3]/div/a[1]")))
        charts=driver.find_element(by=By.XPATH, value="//*[@id='overlap-manager-root']/div[2]/span/div[1]/div/div/div[3]/div/a[1]")
        charts.click()
        #//*[@id="header-toolbar-symbol-search"]
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='header-toolbar-symbol-search']")))
        search=driver.find_element(by=By.XPATH, value="//*[@id='header-toolbar-symbol-search']")
        search.click()
        #//*[@id="overlap-manager-root"]/div/div/div[2]/div/div[2]/div[1]/input
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='overlap-manager-root']/div/div/div[2]/div/div[2]/div[1]/input")))
        searchbar=driver.find_element(by=By.XPATH, value="//*[@id='overlap-manager-root']/div/div/div[2]/div/div[2]/div[1]/input")
        searchbar.clear()
        searchbar.send_keys(TICKER)
        searchbar.send_keys(Keys.ENTER)
        #//*[@id="bottom-area"]/div[4]/div/div[1]/div[1]/div[1]/div[2]/button[1]
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='bottom-area']/div[4]/div/div[1]/div[1]/div[1]/div[2]/button[1]")))
        settings=driver.find_element(by=By.XPATH, value='//*[@id="bottom-area"]/div[4]/div/div[1]/div[1]/div[1]/div[2]/button[1]')
        settings.click()
        trade_size(TRADE_SIZE)
        initial_amount(INITIAL_AMOUNT)
        values={}
        if DEBUG == "T":
            print("Debug mode is on")
            print(f"Timeframe range: {TIMEFRAME_RANGE}")
            try:
                for i in range(0, TIMEFRAME_RANGE):
                    #time.sleep(5)
                    #//*[@id="inputs"]
                   
                    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='bottom-area']/div[4]/div/div[1]/div[1]/div[1]/div[2]/button[1]")))
                    settings=driver.find_element(by=By.XPATH, value='//*[@id="bottom-area"]/div[4]/div/div[1]/div[1]/div[1]/div[2]/button[1]')
                    settings.click()

                    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='inputs']")))
                    inputs=driver.find_element(by=By.XPATH, value="//*[@id='inputs']")
                    inputs.click()
                    #//*[@id="overlap-manager-root"]/div/div/div[1]/div/div[3]/div/div[4]/div/span/span[1]/input
                    #//*[@id="overlap-manager-root"]/div/div/div[1]/div/div[3]/div/div[4]/div/span/span[1]/input
                    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='overlap-manager-root']/div/div/div[1]/div/div[3]/div/div[4]/div/span/span[1]/input")))
                    timeframe=driver.find_element(by=By.XPATH, value="//*[@id='overlap-manager-root']/div/div/div[1]/div/div[3]/div/div[4]/div/span/span[1]/input")
                    if timeframe.get_attribute("value").isdigit():
                        timeframe.send_keys(Keys.BACKSPACE)
                        timeframe.send_keys(Keys.BACKSPACE)
                        timeframe.send_keys(Keys.BACKSPACE)
                    else:

                        timeframe.send_keys(Keys.BACKSPACE)
                    
                    timeframe.send_keys(i)
                    print(f"sent {i} key(s) successfully")
                    print(f"value of timeframe: {timeframe.get_attribute('value')}")
                    #//*[@id="overlap-manager-root"]/div/div/div[1]/div/div[4]/div/span/button
                    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='overlap-manager-root']/div/div/div[1]/div/div[4]/div/span/button")))
                    submit=driver.find_element(by=By.XPATH, value="//*[@id='overlap-manager-root']/div/div/div[1]/div/div[4]/div/span/button")
                    submit.click()
                    #//*[@id="bottom-area"]/div[4]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]
                    #//*[@id="bottom-area"]/div[4]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]
                    time.sleep(2)
                    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='bottom-area']/div[4]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]")))
                    percent=driver.find_element(by=By.XPATH, value="//*[@id='bottom-area']/div[4]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]")
                    percent_value = percent.text
                    print("percent text: "+percent.text)
                    # ... your existing code ...

                    percent_value = percent.text
                    percent_value = re.sub(r'[^\d.-]', '', percent_value)

                    if percent_value:  # check if percent_value is not empty
                        values[i] = float(percent_value)
                    else:
                        print("percent_value is empty")
            except NoSuchElementException:
                print("No such element")
        elif DEBUG == "F":
            print("Debug mode is off")
            try:
                
                for i in range(0, TIMEFRAME_RANGE):
                    #time.sleep(5)
                    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='bottom-area']/div[4]/div/div[1]/div[1]/div[1]/div[2]/button[1]")))
                    settings=driver.find_element(by=By.XPATH, value='//*[@id="bottom-area"]/div[4]/div/div[1]/div[1]/div[1]/div[2]/button[1]')
                    settings.click()

                    #//*[@id="inputs"]
                    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='inputs']")))
                    inputs=driver.find_element(by=By.XPATH, value="//*[@id='inputs']")
                    inputs.click()

                    #//*[@id="overlap-manager-root"]/div/div/div[1]/div/div[3]/div/div[4]/div/span/span[1]/input
                    #//*[@id="overlap-manager-root"]/div/div/div[1]/div/div[3]/div/div[4]/div/span/span[1]/input
                    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='overlap-manager-root']/div/div/div[1]/div/div[3]/div/div[4]/div/span/span[1]/input")))
                    timeframe=driver.find_element(by=By.XPATH, value="//*[@id='overlap-manager-root']/div/div/div[1]/div/div[3]/div/div[4]/div/span/span[1]/input")
                    if timeframe.get_attribute("value").isdigit():
                        timeframe.send_keys(Keys.BACKSPACE)
                        timeframe.send_keys(Keys.BACKSPACE)
                        timeframe.send_keys(Keys.BACKSPACE)
                    else:

                        timeframe.send_keys(Keys.BACKSPACE)
                    
                    timeframe.send_keys(i)
                    #print(f"sent {i} key(s) successfully")
                    print("Successfully sent key to timeframe input")
                    #print(f"value of timeframe: {timeframe.get_attribute('value')}")
                    #//*[@id="overlap-manager-root"]/div/div/div[1]/div/div[4]/div/span/button
                    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='overlap-manager-root']/div/div/div[1]/div/div[4]/div/span/button")))
                    submit=driver.find_element(by=By.XPATH, value="//*[@id='overlap-manager-root']/div/div/div[1]/div/div[4]/div/span/button")
                    submit.click()
                    #//*[@id="bottom-area"]/div[4]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]
                    #//*[@id="bottom-area"]/div[4]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]
                    time.sleep(2)
                    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='bottom-area']/div[4]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]")))
                    percent=driver.find_element(by=By.XPATH, value="//*[@id='bottom-area']/div[4]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]")
                    percent_value = percent.text
                    #print("percent text: "+percent.text)
                    # ... your existing code ...

                    percent_value = percent.text
                    percent_value = re.sub(r'[^\d.-]', '', percent_value)

                    if percent_value:  # check if percent_value is not empty
                        values[i] = float(percent_value)
                    else:
                        print("percent_value is empty")

                # ... your existing code ...
            except NoSuchElementException:
                print("No such element")

        sorted_values = dict(sorted(values.items(), key=lambda item: item[1], reverse=True))

        for key, value in sorted_values.items():
            print(f"Timeframe: {key}, Percent: {value}")

        time.sleep(20)
    except ElementClickInterceptedException as e:
        print(f"{e} was thrown")


if __name__ == "__main__":
    load_dotenv()
    user=os.getenv("USER")

    pswrd=os.getenv("PASSWORD")
    if len(sys.argv) != 6:  # Correct number of arguments including the script name
        print("Usage: python main.py <ticker> <timeframe_range> <initial_amount> <trade_size> <debug(T/F)>")
        sys.exit(1)
    else:
        Ticker = sys.argv[1]
        tf_range = int(sys.argv[2])
        
        ia=sys.argv[3]
        ts=sys.argv[4]
        Debug = sys.argv[5] # T or F
        driver = webdriver.Chrome()
        
        main(Ticker, tf_range, ia,ts,Debug)
