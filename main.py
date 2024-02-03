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

greatest_percent = []
def trade_size(TRADE_SIZE,trade_size_XPATH):
    #//*[@id="inputs"]

    
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='inputs']")))
    inputs=driver.find_element(by=By.XPATH, value="//*[@id='inputs']")
    inputs.click()
    #//*[@id="overlap-manager-root"]/div/div/div[1]/div/div[3]/div/div[18]/div/span/span[1]/input
    
    #WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='overlap-manager-root']/div/div/div[1]/div/div[3]/div/div[18]/div/span/span[1]/input")))
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, trade_size_XPATH)))
    trade_size=driver.find_element(by=By.XPATH, value=trade_size_XPATH)
    trade_size_previous=trade_size.get_attribute("value")
    num_of_backspaces = len(trade_size_previous)

    for _ in range(num_of_backspaces):
        trade_size.send_keys(Keys.BACKSPACE)
    
    trade_size.send_keys(TRADE_SIZE)
    print("Successfully sent trade size")
    
    print(f"Trade size: {TRADE_SIZE}")

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
    print(f"Initial amount: {INITIAL_AMOUNT}")

def strategy(TICKER,TIMEFRAME_RANGE,INITIAL_AMOUNT,TRADE_SIZE,DEBUG,first_ticker):
    global greatest_percent
    print(f"Processing Ticker: {TICKER}")
    if first_ticker == True:
       pass
    else:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='header-toolbar-symbol-search']")))
        search_bar = driver.find_element(by=By.XPATH, value="//*[@id='header-toolbar-symbol-search']")
        search_bar.click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='overlap-manager-root']/div/div/div[2]/div/div[2]/div[1]/input")))
        ticker_input = driver.find_element(by=By.XPATH, value="//*[@id='overlap-manager-root']/div/div/div[2]/div/div[2]/div[1]/input")
        ticker_input.clear()
        ticker_input.send_keys(TICKER)
        ticker_input.send_keys(Keys.ENTER)
 
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='bottom-area']/div[4]/div/div[1]/div[1]/div[1]/div[2]/button[1]")))
    settings=driver.find_element(by=By.XPATH, value='//*[@id="bottom-area"]/div[4]/div/div[1]/div[1]/div[1]/div[2]/button[1]')
    settings.click()
    trade_size(TRADE_SIZE,"//*[@id='overlap-manager-root']/div/div/div[1]/div/div[3]/div/div[6]/div/span/span[1]/input")
    initial_amount(INITIAL_AMOUNT)
    values={}
    #/html/body/div[2]/div[3]/div/div/div[3]/div[1]/div/div/div/div/div[14]/div/div/button[2]
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/div/div/div[3]/div[1]/div/div/div/div/div[14]/div/div/button[2]")))
    """     layout=driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[3]/div/div/div[3]/div[1]/div/div/div/div/div[14]/div/div/button[2]")
    layout.click()
    #//*[@id="overlap-manager-root"]/div/span/div[1]/div/div/div[11]
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='overlap-manager-root']/div/span/div[1]/div/div/div[11]")))
    layout_options=driver.find_element(by=By.XPATH, value="//*[@id='overlap-manager-root']/div/span/div[1]/div/div/div[11]")
    layout_options.click()
    #//*[@id="overlap-manager-root"]/div/div/div[1]/div/div[4]/div/div/div[1]/a/div/div[1]
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='overlap-manager-root']/div/div/div[1]/div/div[4]/div/div/div[1]/a/div/div[1]")))
    layout_options_2=driver.find_element(by=By.XPATH, value="//*[@id='overlap-manager-root']/div/div/div[1]/div/div[4]/div/div/div[1]/a/div/div[1]")
    #//*[@id="overlap-manager-root"]/div/div/div[1]/div/div[4]/div/div/div[1]/a/div
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='overlap-manager-root']/div/div/div[1]/div/div[4]/div/div/div[1]/a/div")))
    layout_options_2_button=driver.find_element(by=By.XPATH, value="//*[@id='overlap-manager-root']/div/div/div[1]/div/div[4]/div/div/div[1]/a/div")
    if(layout_options_2.text == "Testing Alg"):
        print("selecting layout")
        layout_options_2_button.click()
    else:
        print("Cannot find layout... "+layout_options_2.text)
    """
    
    if DEBUG == "T":
        print("Debug mode is on")
        print(f"Timeframe range: {TIMEFRAME_RANGE}")
        try:
            for i in range(1, TIMEFRAME_RANGE+1):
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
                timeframe.send_keys(Keys.ENTER)
                time.sleep(2)
                print(f"sent {i} key(s) successfully for {TICKER}")
                print(f"value of timeframe: {timeframe.get_attribute('value')}")
                #//*[@id="overlap-manager-root"]/div/div/div[1]/div/div[4]/div/span/button
                WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='overlap-manager-root']/div/div/div[1]/div/div[4]/div/span/button")))
                submit=driver.find_element(by=By.XPATH, value="//*[@id='overlap-manager-root']/div/div/div[1]/div/div[4]/div/span/button")
                submit.click()
                #//*[@id="bottom-area"]/div[4]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]
                #//*[@id="bottom-area"]/div[4]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]
                
                WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='bottom-area']/div[4]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]")))
                percent=driver.find_element(by=By.XPATH, value="//*[@id='bottom-area']/div[4]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]")
                percent_value = percent.text
                print("percent text: "+percent.text)
                # ... your existing code ...

                percent_value = percent.text

                percent_value = re.sub(r'[^\d.-]', '', percent_value)

                if percent_value:  # check if percent_value is not empty
                    percent_value_float = float(percent_value)
                    values[i] = percent_value_float

                    # Update greatest_percent
                    existing_entry = next((item for item in greatest_percent if item[1] == TICKER), None)
                    if existing_entry:
                        if percent_value_float > existing_entry[0]:
                            existing_entry[0] = percent_value_float  # Update percent
                            existing_entry[2] = i  # Update timeframe
                    else:
                        # Append new best performance
                        greatest_percent.append([percent_value_float, TICKER, i])

                    # Update ticker_data with the best performance
                    if TICKER not in ticker_data or percent_value_float > ticker_data[TICKER][0]:
                        ticker_data[TICKER] = [percent_value_float, i]  # [Best Percent, Timeframe]
        #//*[@id="header-toolbar-symbol-search"] This is to click on the search bar
        #//*[@id="overlap-manager-root"]/div/div/div[2]/div/div[2]/div[1]/input This is to send the ticker
        except NoSuchElementException:
            print("No such element")
    elif DEBUG == "F":
        print("Debug mode is off")
        try:
            
            for i in range(1, TIMEFRAME_RANGE+1):
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

                #print("percent text: "+percent.text)
                # ... your existing code ...

                percent_value = percent.text
                percent_value = re.sub(r'[^\d.-]', '', percent_value)


                if percent_value:  # check if percent_value is not empty
                    percent_value_float = float(percent_value)
                    values[i] = percent_value_float

                    # Update greatest_percent
                    existing_entry = next((item for item in greatest_percent if item[1] == TICKER), None)
                    if existing_entry:
                        if percent_value_float > existing_entry[0]:
                            existing_entry[0] = percent_value_float  # Update percent
                            existing_entry[2] = i  # Update timeframe
                    else:
                        # Append new best performance
                        greatest_percent.append([percent_value_float, TICKER, i])

                    # Update ticker_data with the best performance
                    if TICKER not in ticker_data or percent_value_float > ticker_data[TICKER][0]:
                        ticker_data[TICKER] = [percent_value_float, i]  # [Best Percent, Timeframe]
            # ... your existing code ...
        except NoSuchElementException:
            print("No such element")

    sorted_values = dict(sorted(values.items(), key=lambda item: item[1], reverse=True))

    for key, value in sorted_values.items():
        print(f"Timeframe: {key}, Percent: {value}")
        ticker_data[TICKER] = sorted_values



def main(TICKER, TIMEFRAME_RANGE, INITIAL_AMOUNT, TRADE_SIZE, DEBUG):
    Username= user
    Password= pswrd
    #Testing a trading strategy by going thru different timeframes to see which yields the best results

    #Set up the driver
    driver.get("https://www.tradingview.com")
    
    
    #/html/body/div[3]/div[3]/div[2]/div[3]/button[1]/svg/path

   
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
        #//*[@id="id_code"]
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='id_code']")))
        code=driver.find_element(by=By.XPATH, value="//*[@id='id_code']")
        code.send_keys(input("Enter the code sent to your DUO: "))

        if code.get_attribute("value") != "":
            login_successful = True
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

        driver.fullscreen_window()
        time.sleep(5)
        #//*[@id="overlap-manager-root"]/div/div/div[2]/div/div/div[1]/div/div[1]/span/form/input
        #/html/body/div[4]/div[3]/div[2]/div[2]/div/div/div/button[1]
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[3]/div[2]/div[2]/div/div/div/button[1]")))
        search_bar=driver.find_element(by=By.XPATH, value="/html/body/div[4]/div[3]/div[2]/div[2]/div/div/div/button[1]")
        
        search_bar.click()
        #//*[@id="overlap-manager-root"]/div/div/div[2]/div/div/div[1]/div/div[1]/span/form/input

        #//*[@id="header-toolbar-symbol-search"] This is to click on the search bar
        #//*[@id="overlap-manager-root"]/div/div/div[2]/div/div[2]/div[1]/input This is to send the ticker
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='overlap-manager-root']/div/div/div[2]/div/div/div[1]/div/div[1]/span/form/input")))
        sending_search=driver.find_element(by=By.XPATH, value="//*[@id='overlap-manager-root']/div/div/div[2]/div/div/div[1]/div/div[1]/span/form/input")
        first_ticker=TICKER[0]
        sending_search.clear()
        sending_search.send_keys(first_ticker)
        sending_search.send_keys(Keys.ENTER)

        print("Testing: "+first_ticker)
        strategy(first_ticker,TIMEFRAME_RANGE,INITIAL_AMOUNT,TRADE_SIZE,DEBUG,True)
        #//*[@id="header-toolbar-symbol-search"]
        #//*[@id="bottom-area"]/div[4]/div/div[1]/div[1]/div[1]/div[2]/button[1]
        
        sorted_ticker = sorted(ticker_data.items(), key=lambda x: max(x[1].values()), reverse=True)
        for TICKER in TICKER[1:]:
            print(f"Prcessing Ticker: {TICKER}")
            
            strategy(TICKER,TIMEFRAME_RANGE,INITIAL_AMOUNT,TRADE_SIZE,DEBUG,False)
        print("Results: ")
        for performance in greatest_percent:
            print(f"Best %: {performance[0]} for {performance[1]} at {performance[2]} Timeframe")
        #print("\nTicker Performance in Descending Order:")
        #for ticker, best_performance in sorted_ticker:
           # print(f"\n{ticker}: Best Performance: {best_performance[0]}% at Timeframe {best_performance[1]}")
    except ElementClickInterceptedException as e:
        print(f"{e} was thrown")


if __name__ == "__main__":
    load_dotenv()
    user=os.getenv("USER")
    ticker_data = {}
    percent=[]

    pswrd=os.getenv("PASSWORD")
    driver = webdriver.Chrome()
   
    options = Options()
    options.add_argument("--headless")
    
    if len(sys.argv) != 6:
        print("Usage: python main.py <tickers> <timeframe_range> <initial_amount> <trade_size> <debug(T/F)>")
        sys.exit(1)
    else:
        tickers = sys.argv[1].split(',')  # Split comma-separated tickers into a list
        tf_range = int(sys.argv[2])
        ia = sys.argv[3]
        ts = sys.argv[4]
        Debug = sys.argv[5]  # T or F

       
        main(tickers, tf_range, ia, ts, Debug)
