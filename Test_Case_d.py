from selenium import webdriver
import requests

driver = webdriver.Firefox()

def open_page():
    """Opening web-page"""
    print("opening page")
    driver.get("http://www.facebook.com/")

def request():
    """Checking status"""
    reques = requests.get('http://www.facebook.com/')
    print reques.status_code

def assert_text(fieldName, fieldText, xPath):
    "checking %s" %("fieldName")
    fieldName = driver.find_element_by_xpath(xPath)
    assert fieldText in fieldName.text
    print("Assertion Completed")

def form_fill(field, xPath, fieldName, fieldText):
    fieldText = driver.find_element_by_xpath(xPath)
    fieldText.send_keys(field)
    print("%s Entered" % (fieldName))

def create_account(fieldText, xPath, fieldName):
    #Creating account
    fieldText = driver.find_element_by_xpath(xPath)
    fieldText.click()
    print("%s Entered" % (fieldName))

def main():
    """Running all the functions"""
    open_page()
    request()
    assert_text("first_name", "First name", '//*[@id="u_0_0"]/div/div')
    assert_text("last_name", "Surname", '//*[@id="u_0_2"]/div/div')
    assert_text("email", "Mobile number or email address", '//*[@id="u_0_5"]/div/div')
    assert_text("email_again", "Re-enter mobile number or email address", '//*[@id="u_0_8"]/div/div')
    assert_text("password", "New password", '//*[@id="u_0_a"]/div/div')
    assert_text("birth_day", "Day", '//*[@id="day"]/option[1]')
    assert_text("birth_month", "Month", '//*[@id="month"]/option[1]')
    assert_text("birth_year", "Year", '//*[@id="year"]/option[1]')
    assert_text("gender_female", "Female", '//*[@id="u_0_h"]/span[1]/label')
    assert_text("gender_male", "Male", '//*[@id="u_0_h"]/span[2]/label')
    form_fill("Mark", '//*[@id="u_0_1"]', "First Name", "first_name")
    form_fill("Zuckerberg", '//*[@id="u_0_3"]', "Last Name", "last_name")
    form_fill("markzukerberg@gmail.com", '//*[@id="u_0_6"]', "Email", "email")
    form_fill("markzukerberg@gmail.com", '//*[@id="u_0_9"]', "Email ID", "email_again")
    form_fill("abcd12345", '//*[@id="u_0_b"]', "Password", "pass_word")
    form_fill(14, '//*[@id="day"]', "Day", "birth_day")
    form_fill("May", '//*[@id="month"]', "Month", "birth_month")
    form_fill(1985, '//*[@id="year"]', "Year", "birth_year")
    create_account("sex", '//*[@id="u_0_f"]', "Gender")
    create_account("button", '//*[@id="u_0_j"]', "Account")

main()