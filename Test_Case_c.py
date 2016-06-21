from selenium import webdriver
import time

driver = webdriver.Firefox()

def open_page():
    driver.get("http://www.python.org")

def reach_sign_up_page():
    element = driver.find_element_by_xpath('//*[@id="touchnav-wrapper"]/header/\
        div/div[1]/div[3]/ul/li/a')
    element.click()
    print("clicked on element")

    element_again = driver.find_element_by_xpath('//*[@id="content"]/div/aside/\
        div/p[2]/a')
    element_again.click()
    print("clicked on element_again")

def assertion():
    user = driver.find_element_by_xpath('//*[@id="signup_form"]/p[1]/label')
    assert "Username:" in user.text
    print "Username assertion complete"

    mail = driver.find_element_by_xpath('//*[@id="signup_form"]/p[2]/label')
    assert "E-mail:" in mail.text
    print "Email assertion complete"

    password = driver.find_element_by_xpath('//*[@id="signup_form"]/p[3]/label')
    assert "Password:" in password.text
    print "Password assertion complete"

    password_again = driver.find_element_by_xpath('//*[@id="signup_form"]/p[4]/label')
    assert "Password (again):" in password_again.text
    print "Password_again assertion complete"

def form_fill_up():
    username = driver.find_element_by_id('id_username')
    username.send_keys("Abcd")
    print("filled username")

    email = driver.find_element_by_id('id_email')
    email.send_keys("abcd@gmail.com")
    print("entered email")

    pass1 = driver.find_element_by_id('id_password1')
    pass1.send_keys("abcd12345")
    print("entered password1")

    pass2 = driver.find_element_by_id('id_password2')
    pass2.send_keys("abcd12345")
    print("entered password2")

def created_form():
    sign_up = driver.find_element_by_xpath('//*[@id="signup_form"]/button')
    time.sleep(5)
    sign_up.click()
    print("created form")

def main():
    open_page()
    reach_sign_up_page()
    assertion()
    form_fill_up()
    created_form()



if __name__ == "__main__":
    main()
    print "done"