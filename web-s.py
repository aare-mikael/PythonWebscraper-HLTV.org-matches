from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

dates=[]
times=[]
events=[]
matchlengths=[]
hometeams=[]
awayteams=[]
driver.get("https://www.hltv.org/matches")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a', href=True, attrs={'class':'upcomingMatchesSection'}):
    date=a.find('div', attrs={'class':'matchDayHeadline'})
    dates.append(date.text)
    for b in soup.findAll('b', href=True, attrs={'class':'upcomingMatch removeBackground' | 'upcomingMatch removeBackground oddRowBgColor'}):
        time=b.find('div', attrs={'class':'matchTime'})
        event=b.find('div', attrs={'class':'matchEventName gtSmartphone-only'})
        matchlength=b.find('div', attrs={'class':'matchMeta'})
        hometeam=b.find('div', attrs={'class':'matchTeamName text-ellipsis'})
        awayteam=b.find('div', attrs={'class':'matchTeamName text-ellipsis'})

        times.append(time.text)
        events.append(event.text)
        matchlengths.append(matchlength.text)
        hometeams.append(hometeam.text)
        awayteams.append(awayteam.text)

df = pd.DataFrame({
    'Date' : dates, 
    'Time' : times, 
    'Event' : events, 
    'Match length' : matchlengths, 
    'Home team' : hometeams, 
    'Away team' : awayteams
    })

df.to_excel(r'C:\Users\Ukjendt\OneDrive\Programmeringsprosjekter\Webscraper Python\Uthenta\Matches.xlsx', index = False, header=True)