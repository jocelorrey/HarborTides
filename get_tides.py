from bs4 import BeautifulSoup
from datetime import date
from location.state import State
from location.harbor import Harbor
from utilities.scraper import Scraper
from utilities.parser import TableParser



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

# Configure & run web scraper
scrap = Scraper(url)
scrap._set_goal("table", {"class": "tides"})
scrap._set_error_msg("Oops! That page can’t be found.")

tide_table = scrap._scrape()

# Configure parser
parser = TableParser(tide_table)
parser._set_output_key_val_indices(0, [2, 4, 6, 8, 10, 11])

# Deal with errors
while not parser._valid_input:
  print("The harbor you searched for cannot be found.")
  try_again = input('Try again? [y/n] ').lower()
  if try_again in ['y', 'yes']:
    url = get_search_url()
    tide_table = scrap._scrape(url)
    parser._set_table(tide_table)
  else:
    quit()

# Run parser
daily_tides = parser._parse_to_dict()

today = date.today().strftime("%d")
result = daily_tides[today]
[high_am, high_pm, low_am, low_pm, sunrise, sunset] = result

print("Today's high tides:", set_AM(high_am), set_PM(high_pm))

"""
Useful Resources:
1. Tutorial: https://www.edureka.co/blog/web-scraping-with-python/
2. Beautiful Soup Docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
3. Beautiful Soup - Find Table: https://stackoverflow.com/questions/33766740/beautifulsoup-find-table-with-specified-class-on-wikipedia-page
4. Beautiful Soup - Parsing Table: https://pythonprogramming.net/tables-xml-scraping-parsing-beautiful-soup-tutorial/
5. ASCII Waves: https://ascii.co.uk/art/wave

Tide Table Row Format:
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