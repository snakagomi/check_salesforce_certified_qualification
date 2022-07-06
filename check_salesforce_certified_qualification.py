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
    update_date_month = update_date.month
    current_month = datetime.now().month
    is_current_month = check_current_month(update_date_month, current_month)
    if is_current_month:
        CHROME_DRIVER.find_element(By.XPATH, "//*[@id=\"layout\"]/ul[2]/li[7]/a").click()
    else:
        CHROME_DRIVER.close()


def get_update_date_block():
    update_date_block = CHROME_DRIVER.find_element(By.XPATH, "//*[@id=\"layout\"]/p").text
    return update_date_block


def split_by_linefeed_code(string):
    split_block = re.split('\n', string)
    return split_block


def split_by_colon(string):
    split_string = re.split(":", string)
    update_date = split_string[1].replace(' ', '')
    return update_date


def check_current_month(compared_month, comparing_month):
    if compared_month == comparing_month:
        return True
    else:
        return False


# ガター内の緑色のボタンを押すとスクリプトを実行します。
if __name__ == '__main__':
    main()
