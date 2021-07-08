from selenium import webdriver
from bs4 import BeautifulSoup


def get_state_abbrev(state_name):
  ocean_states = {'alabama': 'AL', 'alaska': 'AK', 'california': 'CA',
  'connecticut': 'CT', 'delaware': 'DE', 'florida': 'FL', 'georgia': 'GA',
  'hawaii': 'HI', 'louisiana': 'LA', 'maine': 'ME', 'maryland': 'MD',
  'massachusetts': 'MA', 'mississippi': 'MS', 'new hampshire': 'NH',
  'new jersey': 'NJ', 'new york': 'NY', 'north carolina': 'NC',
  'oregon': 'OR', 'rhode island': 'RI', 'south carolina': 'SC',
  'texas': 'TX','vermont': 'VT', 'virginia': 'VA', 'washington': 'WA'}

  state = state_name.lower()
  if state in ocean_states.keys():
    return ocean_states[state]
  else:
    return ''

def get_search_url():
  # Get user input
  state = input("US State: ").lower()
  harbor = input("Harbor: ").lower()

  # Clean up user input
  if 'harbor' not in harbor:
    harbor += " harbor"

  while len(state) != 2:
    state = get_state_abbrev(state)
    if state  == '':
      state = input("Please enter a valid US state bordering the ocean: ").lower()

  # Generate url
  harbor_location = (harbor.replace(' ', '-') + '-' + state)
  return 'https://www.usharbors.com/harbor/' + state + '/' + harbor_location + '/tides#monthly-tide-chart'

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
  

# Execution
# For testing:
# bad_url = 'https://www.usharbors.com/harbor/pa/newark-harbor-pa/tides#monthly-tide-chart'
# good_url = 'https://www.usharbors.com/harbor/maine/york-harbor-me/tides/'

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

print("Woo - got a valid url!")

"""
Useful Resources:
1. Tutorial: https://www.edureka.co/blog/web-scraping-with-python/
2. Beautiful Soup Docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
3. Beautiful Soup - Find Table: https://stackoverflow.com/questions/33766740/beautifulsoup-find-table-with-specified-class-on-wikipedia-page
"""