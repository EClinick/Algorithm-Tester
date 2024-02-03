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


def find_shadow_element(shadow_host_selector, shadow_element_selector):
    shadow_host = driver.find_element(By.CSS_SELECTOR, shadow_host_selector)
    shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)
    return shadow_root.find_element(By.CSS_SELECTOR, shadow_element_selector)

def find_shadow_elements(shadow_host_selector, shadow_element_selector):
    shadow_host = driver.find_element(By.CSS_SELECTOR, shadow_host_selector)
    shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)
    return shadow_root.find_elements(By.CSS_SELECTOR, shadow_element_selector)

def BarChart():
    url = "https://www.barchart.com/stocks/most-active/price-volume-leaders?orderBy=priceVolume&orderDir=desc"
    
    driver.get(url)
    
    # Wait for the elements to be present
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'your-shadow-host-selector'))
    )
    
    # Selectors will need to be updated to match the actual shadow host and element selectors
    shadow_host_selector = 'your-shadow-host-selector'  # You need to fill this in
    symbol_element_selector = 'your-symbol-element-selector'  # You need to fill this in
    
    symbols = []
    symbol_elements = find_shadow_elements(shadow_host_selector, symbol_element_selector)
    for element in symbol_elements:
        symbols.append(element.text)
    
    print(symbols)

if __name__ == "__main__":
    driver = uc.Chrome()
    try:
        BarChart()
    finally:
        try:
            driver.quit()
        except Exception as e:
            print("Error closing driver:", e)