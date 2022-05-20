from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from urllib import request

# CHROME_DRIVER = webdriver.Chrome(ChromeDriverManager().install())
URL = 'https://tandc.salesforce.com/certificate-holder'


def main():
    update_date = get_update_date()
    print(update_date)


def get_update_date():
    response = request.urlopen(URL)
    soup = BeautifulSoup(response)
    response.close()
    exam = soup.find('div', class_='content clearfix')
    return exam


# ガター内の緑色のボタンを押すとスクリプトを実行します。
if __name__ == '__main__':
    main()
