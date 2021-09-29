from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
dates=[]
times=[]
events=[]
hometeams=[]
awayteams=[]
matchlengths=[]
driver.get("https://www.hltv.org/matches")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a', href=True, attrs={'class':'upcomingMatchesSection'}):
    date=a.find('div', attrs={'class':'matchDayHeadline'})
    dates.append(date.text)
    