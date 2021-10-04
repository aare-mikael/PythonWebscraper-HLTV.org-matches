from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import xlwings as xw

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
        matchlength=b.find('div', attrs={'class':'matchMeta'})
        if (b.find('div', attrs={'class':'matchInfoEmpty'})):
            hometeamtext = 'TBD'
            awayteamtext = 'TBD'
            event = b.find('span', attrs={'class':'line-clamp-3'})
            eventtext = event.text
        else:
            hometeam = b.find('div', attrs={'class':'matchTeam team1'})
            hometeamtext = hometeam.text
            awayteam = b.find('div', attrs={'class':'matchTeam team2'})
            awayteamtext = awayteam.text
            event=b.find('div', attrs={'class':'matchEventName gtSmartphone-only'})
            eventtext = event.text
        
        dates.append(date.text)
        times.append(time.text)
        events.append(eventtext)
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

# Closing chrome window opened by driver.get("https://www.hltv.org/matches")
print("Closing Chrome window")
driver.quit()

# Writing CSV-files for easier use later
print("Writing CSV file")
df.to_csv('Uthenta/Matches.csv', encoding='utf-8')

wb = xw.Book()

sheet = wb.sheets["Ark1"] # I have Excel in norwegian, ark means sheet
sheet.name = "Matches"
sheet.api.Tab.Color = 0x70AD47

sheet.range("A1").options(Index=False).value = df

all_data_range = sheet.range("A1").expand('table')
all_data_range.row_height = 30
all_data_range.column_width = 18
all_data_range.color = (240,240,240)
all_data_range.api.Font.Name = 'Arial'
all_data_range.api.Font.Size = 8
all_data_range.api.HorizontalAlignment = xw.constants.HAlign.xlHAlignCenter
all_data_range.api.VerticalAlignment = xw.constants.HAlign.xlHAlignCenter
all_data_range.api.WrapText = True

header_range = sheet.range("A1").expand('right')
header_range.color = (125,255,100)
header_range.api.Font.Color = 0xFFFFFF
header_range.api.Font.Bold = True
header_range.api.Font.Size = 9

id_column_range = sheet.range("A2").expand('down')
id_column_range.color=(198,224,180)

data_ex_headers_range = sheet.range("A2").expand('table')

for border_id in range(7,13):
    data_ex_headers_range.api.Borders(border_id).Weight = 2
    data_ex_headers_range.api.Borders(border_id).Color = 0xFFFFFF

# Saving workbook to Excel
print("Writing xlsx-file")
wb.save(r"Uthenta\Matches.xlsx")