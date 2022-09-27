import log_in
import get_content
import web_driver
import search

driver = web_driver.Driver()

log_in.login(driver)
print("Logged in")

search.search(driver)
print("Searched")

get_content.feed(driver)
print("Feed recieved")
driver.close()
