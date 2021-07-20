from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import date
from location.state import State
from location.harbor import Harbor

## Helper functions
def get_search_url():
  # Get user input
  state = State(input("US State: "))
  while state.abbrev is None:
      state = State(input("Please enter a valid US state bordering the ocean: "))
  harbor = Harbor(input("Harbor: "))

  # Generate url
  harbor_location = harbor.name + '-' + state.abbrev
  return 'https://www.usharbors.com/harbor/' + state.abbrev + '/' + harbor_location + '/tides#monthly-tide-chart'

def get_tide_table(search_url):
  driver = webdriver.Chrome()
  driver.get(search_url)
  content = driver.page_source
  soup = BeautifulSoup(content, 'html.parser')

  if soup.h1.string == 'Oops! That page can’t be found.':
    driver.close()
    return None

  else:
    driver.close()
    return soup.find("table", {"class": "tides"})
  
def set_AM(time_str):
  if time_str == '':
    return None
  return time_str + ' AM'

def set_PM(time_str):
  if time_str == '':
    return None
  return time_str + ' PM'

## Main Execution
url = get_search_url()
tide_table = get_tide_table(url)

# Deal with errors
while tide_table is None:
  print("The harbor you searched for cannot be found.")
  try_again = input('Try again? [y/n] ').lower()
  if try_again in ['y', 'yes']:
    url = get_search_url()
    tide_table = get_tide_table(url)
  else:
    quit()

# Get current date & time
now = date.today()
current_day = now.strftime("%d") # ex. 19
#current_month = now.strftime("%b") # ex. Jul
#current_year = now.strftime("%Y") # ex. 2021

# Parse tide table
daily_tides = {}
table_rows = tide_table.find_all('tr')
for row in table_rows:
    table_data = row.find_all('td')
    row = [i.text for i in table_data]
    """
    Row format:
    ['1', 'Thu', '5:22', '8.0', '6:03', '7.9', '11:35', '0.4', '', '', '5:01', '8:28', '', '1', 'Thu']
    0. Day of month (valid for current month)
    1. Day of week
    2. Time of high tide (AM)
    3. Height of high tide (ft)
    3. Time of high tide (PM)
    4. Height of high tide (ft)
    5. Time of low tide (AM)
    6. Height of low tide (ft)
    7. Time of low tide (PM)
    8. Height of low tide (ft)
    9. Sunrise time (AM)
    10. Sunset time (PM)
    11. Moon phase (seems to always be blank)
    12. Day of month again
    13. Day of week again
    """
    if len(row) != 0:
      day = row[0]
      high_tides = (set_AM(row[2]), set_PM(row[4]))
      low_tides = (set_AM(row[6]), set_PM(row[8]))
      sun_rise_set = (set_AM(row[10]), set_PM(row[11]))
      daily_tides[day] = [high_tides, low_tides, sun_rise_set]

[htides_today, ltides_today, sun_today] = daily_tides[current_day]

print("   ,(   ,(   ,(   ,(   ,(   ,(  ")
print("`-'  `-'  `-'  `-'  `-'  `-'  `-")
print("--- " + now.strftime("%d %b %Y") + " Tidal Data: ---")
print("High tides:", htides_today[0], "and", htides_today[1])
print("Low tides: ", ltides_today[0], "and", ltides_today[1])
print("Sunrise:   ", sun_today[0])
print("Sunset:    ", sun_today[1])

"""
Useful Resources:
1. Tutorial: https://www.edureka.co/blog/web-scraping-with-python/
2. Beautiful Soup Docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
3. Beautiful Soup - Find Table: https://stackoverflow.com/questions/33766740/beautifulsoup-find-table-with-specified-class-on-wikipedia-page
4. Beautiful Soup - Parsing Table: https://pythonprogramming.net/tables-xml-scraping-parsing-beautiful-soup-tutorial/
5. ASCII Waves: https://ascii.co.uk/art/wave
"""