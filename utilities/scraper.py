from selenium import webdriver
from bs4 import BeautifulSoup

class Scraper:
  
  def __init__(self, url, driver=webdriver.Chrome()):
    self._url = url
    self._goal_type = None
    self._goal_vals = None
    self._error_msg = None
    self._driver = driver

    self._error = None
  
  def _set_url(self, url):
    self._url = url

  def _set_goal(self, type, vals):
    self._goal_type = type
    self._goal_vals = vals

  def _set_error_msg(self, msg):
    self._error_msg = msg
  
  def _error_found(self, soup):
    return soup.h1.string == self._error_msg

  def _scrape(self, **kwargs):
    url = kwargs.get('url', self._url)
    self._driver.get(url)
    content = self._driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    self._driver.close()
    
    if self._error_found(soup):
      self._error = True
      return None
    
    self._error = False
    return soup.find(self._goal_type, self._goal_vals)
