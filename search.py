import web_driver
import time
driver = web_driver

tags = ["van life", "converted van", "van living"]
comments = ["Great post!", "Love this!", "<3", "Keep the posts coming!"]
no_of_photos = 5

photo_details_dict = {}


def search(driver):
    for tag in tags:
        # search box
        driver.type_in_box("XPATH", "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[2]/input", f"\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b{tag}\n")
        # driver.type_in_box("XPATH",
        #                    "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[2]/input",
        #                    f"\n")
        # time.sleep(5)
        # driver.refresh()
        # pictures = driver.select_all("section article img")

        # search button
        driver.click("XPATH", "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/div[1]/div/a/div/div[2]/div/div/div")

        # first picture
        driver.click("XPATH", "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[2]/div[1]/div/div[1]/div[2]/div/a/div/div[2]")

        # for picture in pictures:
        #     print(picture)
        #     driver.click("SELECTOR", picture)
        #     print("clicked on picture")
        #     driver.click("XPATH", "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]")
        #     print("clicked like button")


        counter = 0
        while counter < no_of_photos:
            # like button
            driver.click("XPATH", "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]")
            # next photo button
            # try: driver.click("XPATH", "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[2]/div[1]/div/div[1]/div[2]/div/a/div/div[2]")
            #
            # except:
            
            # comments
            driver.click("XPATH", "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea")
            driver.type_in_box("XPATH", "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea", comments[counter])
            driver.click("XPATH","/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button/div")
            # next photo button
            # driver.click("XPATH", "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[2]/div[1]/div/div[1]/div[2]/div/a/div/div[2]")
            try:
                # this one doesn't work every time for some reason
                driver.click("XPATH", "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button/div/span")
            #     is this excpet too vague?
            except:
                driver.click("XPATH", "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button/div/span")

            counter += 1