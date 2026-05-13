from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://selenium.dev")
driver.quit()

if __name__=='__main__':
    pass