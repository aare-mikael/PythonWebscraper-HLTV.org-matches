from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import asyncio

# async def findDates(soup, dates, times, events, matchlengths, hometeams, awayteams):
#     for a in soup.findAll('a', href=True, attrs={'class':'upcomingMatchesSection'}):
#         date=a.find('div', attrs={'class':'matchDayHeadline'})
#         dates.append(date.text)
#         print(date)
#         print("Calling findDetails")
#         for b in soup.findAll('b', href=True, attrs={'class':'upcomingMatch removeBackground'}):
#             time=b.find('div', attrs={'class':'matchTime'})
#             event=b.find('div', attrs={'class':'matchEventName gtSmartphone-only'})
#             matchlength=b.find('div', attrs={'class':'matchMeta'})
#             hometeam=b.find('div', attrs={'class':'matchTeamName text-ellipsis'})
#             awayteam=b.find('div', attrs={'class':'matchTeamName text-ellipsis'})
#             print("We're in for b")

#             times.append(time.text)
#             events.append(event.text)
#             matchlengths.append(matchlength.text)
#             hometeams.append(hometeam.text)
#             awayteams.append(awayteam.text)

# async def findDetails(soup, dates, times, events, matchlengths, hometeams, awayteams):
#     for b in soup.findAll('b', href=True, attrs={'class':'upcomingMatch removeBackground'}):
#         time=b.find('div', attrs={'class':'matchTime'})
#         event=b.find('div', attrs={'class':'matchEventName gtSmartphone-only'})
#         matchlength=b.find('div', attrs={'class':'matchMeta'})
#         hometeam=b.find('div', attrs={'class':'matchTeamName text-ellipsis'})
#         awayteam=b.find('div', attrs={'class':'matchTeamName text-ellipsis'})
#         print("We're in for b")

#         times.append(time.text)
#         events.append(event.text)
#         matchlengths.append(matchlength.text)
#         hometeams.append(hometeam.text)
#         awayteams.append(awayteam.text)

# async def collectMatches():

dates = []
times = []
events = []
matchlengths = []
hometeams = []
awayteams = []

driver = webdriver.Chrome('C:/bin/chromium-browser/chromedriver.exe')
driver.get("https://www.hltv.org/matches")
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

for a in soup.find_all('div', class_='upcomingMatchesSection'):
    date=a.find('div', class_='matchDayHeadline')
    # for b in a('div', class_='upcomingMatch removeBackground'):
    for b in a('div', class_=['upcomingMatch removeBackground oddRowBgColor', 'upcomingMatch removeBackground']):
        time=b.find('div', attrs={'class':'matchTime'})
        event=b.find('div', attrs={'class':'matchEventName gtSmartphone-only'})
        matchlength=b.find('div', attrs={'class':'matchMeta'})
        hometeam = b.find('div', attrs={'class':'matchTeam team1'})
        print(hometeam)
        print(hometeam.text)
        awayteam = b.find('div', attrs={'class':'matchTeam team2'})
        print(awayteam)
        dates.append(date.text)
        times.append(time.text)
        events.append(event)
        matchlengths.append(matchlength.text)
        hometeams.append(hometeam.text)
        awayteams.append(awayteam.text)

print("Done collecting all data, creating DataFrame now")
df = pd.DataFrame({
    'Date' : dates, 
    'Time' : times, 
    'Event' : events, 
    'Match length' : matchlengths, 
    'Home team' : hometeams, 
    'Away team' : awayteams
    })

print("Writing Excel file")
df.to_excel(r'C:\Users\Ukjendt\OneDrive\Programmeringsprosjekter\Webscraper Python\Uthenta\Matches.xlsx', index = False, header=True)