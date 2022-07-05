from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import re

CHROME_DRIVER = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
URL = 'https://tandc.salesforce.com/certificate-holder'
CHROME_DRIVER.get("https://tandc.salesforce.com/certificate-holder")


def main():
    update_date_block = get_update_date_block()
    split_block = split_by_linefeed_code(update_date_block)
    update_date = split_by_colon(split_block[2])
    update_date = datetime.strptime(update_date, "%Y年%m月%d日")
    current_month = datetime.now().month
    # if update_date == current_month:
    if update_date == 6:
        CHROME_DRIVER.find_element(By.XPATH,"//*[@id=\"layout\"]/ul[2]/li[7]/a").click()


def get_update_date_block():
    update_date_block = CHROME_DRIVER.find_element(By.XPATH, "//*[@id=\"layout\"]/p").text
    return update_date_block


def split_by_linefeed_code(string):
    split_block = re.split('\n', string)
    return split_block


def split_by_colon(string):
    update_date = re.split(":", string)
    return update_date[1].replace(' ', '')


# ガター内の緑色のボタンを押すとスクリプトを実行します。
if __name__ == '__main__':
    main()
