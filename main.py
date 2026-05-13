from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://selenium.dev")
driver.quit()

def main():
    pass

if __name__=='__main__':
    main()