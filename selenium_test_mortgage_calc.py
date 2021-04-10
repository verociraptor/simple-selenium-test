from selenium import webdriver #access the browser
from selenium.webdriver.common.keys import Keys #allow the use of keyboard keys on the browser site
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time # allow browser to stall for a set time before closing

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.mortgagecalculators.info/calc-monthlypayment.php") #gets access to the website
print(driver.title) #will show title of website

try:
    home_price = driver.find_element_by_id("propprice") # element to enter amount of the home price
    home_price.send_keys("335000")

    down_paymnt = driver.find_element_by_id("downamt") # element to enter amount of the down payment
    down_paymnt.send_keys("65000")

    annual_int_rate = driver.find_element_by_name("param[interest_rate]")
    annual_int_rate.send_keys("5")

    loan_term = driver.find_element_by_name("param[loan_term]")
    loan_term.send_keys("10")


    calculate = driver.find_element_by_name("param[calculate]")
    calculate.click()
    time.sleep(30)
except:
    print("error occurred. exiting website")
    driver.quit()
