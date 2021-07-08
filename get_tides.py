from selenium import webdriver
from bs4 import BeautifulSoup
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

print("Woo - got a valid url!")

"""
Useful Resources:
1. Tutorial: https://www.edureka.co/blog/web-scraping-with-python/
2. Beautiful Soup Docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
3. Beautiful Soup - Find Table: https://stackoverflow.com/questions/33766740/beautifulsoup-find-table-with-specified-class-on-wikipedia-page
"""