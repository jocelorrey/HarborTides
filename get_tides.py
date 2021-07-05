from selenium import webdriver
from bs4 import BeautifulSoup


def scrape_data(harbor, state):
  harbor_location = (harbor.replace(' ', '-') + '-' + state).lower() # ex. "York Harbor" + "ME" -> "york-harbor-me"

  driver = webdriver.Chrome()
  driver.get('https://www.usharbors.com/harbor/' + state + '/' + harbor_location + '/tides#monthly-tide-chart')
  content = driver.page_source
  soup = BeautifulSoup(content, 'html.parser')

  tide_table = soup.find("table", {"class": "tides"})
  print("tide_table:", tide_table)
  

# Execution
harbor = input("Harbor: ") # ex. "York Harbor"
state = input("State: ") # ex. "ME"
scrape_data(harbor, state)

"""
Useful Resources:
1. Tutorial: https://www.edureka.co/blog/web-scraping-with-python/
2. Search Bar Query: https://datascience.stackexchange.com/questions/11730/how-to-scrape-a-website-with-a-searchbar
3. HTTPResponse Objects: https://docs.python.org/3/library/http.client.html
4. Beautiful Soup - Find Table: https://stackoverflow.com/questions/33766740/beautifulsoup-find-table-with-specified-class-on-wikipedia-page
"""