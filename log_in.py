import time

account = "your account here"
password = "your password here"


def login(driver):
    driver.get_page("https://www.instagram.com/accounts/login/")
    # allow cookies
    driver.click("XPATH", "/html/body/div[4]/div/div/button[1]")
    driver.type_in_box("SELECTOR", "#loginForm > div > div:nth-child(1) > div > label > input", account)
    driver.type_in_box("SELECTOR", "#loginForm > div > div:nth-child(2) > div > label > input", password)
    driver.click("SELECTOR", "#loginForm > div > div:nth-child(3) > button > div")
    # save login info
    driver.click("XPATH", "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div/section/div/button")
    # turn on notifications
    driver.click("XPATH", "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")

