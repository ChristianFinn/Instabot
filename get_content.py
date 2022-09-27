from bs4 import BeautifulSoup

def feed(driver):
    source = driver.source()
    soup = BeautifulSoup(source, 'html.parser')
    print(soup.prettify())
    pictures = soup.findAll("img", class_ = "_aagt")
    for picture in pictures:
        print(picture)