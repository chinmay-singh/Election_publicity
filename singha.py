#importig libraries
import time
import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def pipeline(email,password):
    search = driver.find_elements_by_id('email')[0].clear()
    search = driver.find_elements_by_id('email')[0]
    search.send_keys(email)
    search = driver.find_elements_by_id('pass')[0].clear()
    search = driver.find_elements_by_id('pass')[0]
    search.send_keys(password)
    search.send_keys(Keys.RETURN)

    singha = driver.find_elements_by_xpath("//input[@placeholder='Search']")[0]
    singha.send_keys("Apruv Gupta")
    singha.send_keys(Keys.RETURN)

    timeline = driver.find_elements_by_xpath("//a[contains(text(), 'Apurv Gupta')]")[0]
    timeline.click()

    SCROLL_PAUSE_TIME = 0.5

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down t
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    comment_placeholder = driver.find_elements_by_xpath("//form[@class='commentable_item']")[0]
    comment = comment_placeholder.find_elements_by_xpath("//div[@role='textbox']")

    for i in range(1,20):
        try:
            comment[i].send_keys("#Apurv_for_gsec_sports")
            time.sleep(random.randint(1,100))
            comment[i].send_keys(Keys.RETURN)
        except:
            pass

if __name__ == "__main__":
    print("Enter facebook email id: ")
    email = str(input())
    password = getpass.getpass("Enter facebook password: ")

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_options=chrome_options)

    driver.get('https://www.facebook.com/') 

    pipeline(email,password)   








    
