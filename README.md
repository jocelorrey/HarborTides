# Harbor Tides

### Purpose

Simple little project to practice web scraping. Gets tidal data for a specified harbor from www.usharbors.com.

### To Run:

1. Run `python3 ./get_tides.py`
2. When prompted, enter a harbor and the two-letter abbreviation for the state in which it is located
   (ex: "Portsmouth Harbor" and "NH")
3. The program navigates to the tides tab for your harbor of interest on www.usharbors.com and grabs the tide table html. Currently it just prints the html as a placeholder. Eventually it'll do something cooler with it (ex. maybe make a simple API where you can run different commands to get high tide for today, low tide for the 17th of the month, etc.)
