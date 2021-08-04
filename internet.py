from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# para rodar o chrome em 2º plano
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.headless = True # also works
browser = webdriver.Chrome(options=chrome_options)
def get_dolar():
    browser.get('https://www.google.com/search?q=dolar&oq=dolar&aqs=chrome..69i57.898j0j4&sourceid=chrome&ie=UTF-8')
    dolar = browser.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
    return dolar

def get_euro():
    browser.get('https://www.google.com/search?q=euro&ei=kg3uYND0GsOp1sQPtaK9kAw&oq=euro&gs_lcp=Cgdnd3Mtd2l6EAMyBwgAELEDEEMyBQgAELEDMgQIABBDMgQIABBDMgUILhCxAzIFCAAQsQMyBAgAEEMyBAgAEEMyBQgAELEDMgIIADoHCAAQRxCwAzoKCC4QsAMQQxCTAjoHCAAQsAMQQzoHCC4QQxCTAjoLCC4QsQMQxwEQowI6CAgAELEDEIMBSgQIQRgAUI28BVjTvgVg-L8FaANwAngAgAFyiAHBA5IBAzAuNJgBAKABAaoBB2d3cy13aXrIAQrAAQE&sclient=gws-wiz&ved=0ahUKEwjQhd-0huHxAhXDlJUCHTVRD8IQ4dUDCA4&uact=5')
    euro =browser.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
    return euro