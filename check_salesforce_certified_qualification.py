from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from urllib import request

CHROME_DRIVER = webdriver.Chrome(ChromeDriverManager().install())
URL = 'https://tandc.salesforce.com/certificate-holder'


def main():
    update_date = get_update_date()
    print(update_date)


def get_update_date():
    CHROME_DRIVER.get("https://tandc.salesforce.com/certificate-holder")
    update_date = CHROME_DRIVER.find_element(By.XPATH, "//*[@id=\"layout\"]/p").text
    return update_date


# ガター内の緑色のボタンを押すとスクリプトを実行します。
if __name__ == '__main__':
    main()
