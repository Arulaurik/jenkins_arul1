from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_init_chrome_browser():
    s=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=s)
    driver.get("http://www.fb.com")
    driver.maximize_window()
    fb_title=driver.title
    assert fb_title=="Facebook – log in or sign up"
