from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
pics=[] # Memes that are pictures
videos=[] # Memes that are gifs
driver.get("https://www.reddit.com/r/dankmemes/")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a', href=True, attrs={'class':'_31qSD5'}):
    fafafaf
