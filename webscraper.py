from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# Defining arrays to put the data in
dates = []
times = []
events = []
matchlengths = []
hometeams = []
awayteams = []

# These 4 lines is what loads the webpage and its info
driver = webdriver.Chrome('C:/bin/chromium-browser/chromedriver.exe')
driver.get("https://www.hltv.org/matches")
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

# These for-loops finds the data with .find, and then appends them to the arrays using .append
# Had to create an if-else when some matches collected didn't know what teams were playing yet because of missing tags
for a in soup.find_all('div', class_='upcomingMatchesSection'):
    date=a.find('div', class_='matchDayHeadline')
    for b in a('div', class_=['upcomingMatch removeBackground oddRowBgColor', 'upcomingMatch removeBackground']):
        time=b.find('div', attrs={'class':'matchTime'})
        event=b.find('div', attrs={'class':'matchEventName gtSmartphone-only'})
        matchlength=b.find('div', attrs={'class':'matchMeta'})
        if (b.find('div', attrs={'class':'matchInfoEmpty'})):
            hometeamtext = 'TBD'
            awayteamtext = 'TBD'
        else:
            hometeam = b.find('div', attrs={'class':'matchTeam team1'})
            hometeamtext = hometeam.text
            awayteam = b.find('div', attrs={'class':'matchTeam team2'})
            awayteamtext = awayteam.text
        
        dates.append(date.text)
        times.append(time.text)
        events.append(event)
        matchlengths.append(matchlength.text)
        hometeams.append(hometeamtext)
        awayteams.append(awayteamtext)

# All data collected, now the DataFrame will be created
print("Done collecting all data, creating DataFrame now")
df = pd.DataFrame({
    'Date' : dates, 
    'Time' : times, 
    'Event' : events, 
    'Match length' : matchlengths, 
    'Home team' : hometeams, 
    'Away team' : awayteams
    })

# Writing CSV-files for easier use later
print("Writing CSV file")
df.to_csv('Uthenta/Matches.csv', encoding='utf-8')

# Writing Excel-files for easier readability
print("Writing Excel file")
df.to_excel('Uthenta/Matches.xlsx', encoding='utf-8')