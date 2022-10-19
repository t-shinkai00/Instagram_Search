import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
wd = webdriver.Chrome(chrome_options=options)

from variables import TARGET_URL, INPUT_SELECTOR, SEARCH_SELECTOR, IG_URL_SELECTOR

def get_ig_urls(key):
  wd.get(TARGET_URL)
  wd.find_element("css selector", INPUT_SELECTOR).send_keys(key)
  wd.find_element("css selector", SEARCH_SELECTOR).click()
  time.sleep(1)

  # 投稿を取得
  urls = map(lambda x: x.get_attribute('href'), wd.find_elements("css selector", IG_URL_SELECTOR))
  account_urls = list(filter(lambda x: x.split("/")[3] != "explore", urls))
  return account_urls