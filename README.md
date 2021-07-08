# Harbor Tides

### Purpose

Simple little project to practice web scraping. Gets tidal data for a specified harbor from www.usharbors.com.

### To Run:

1. Run `python3 ./get_tides.py`
2. When prompted, enter a harbor and the two-letter abbreviation or full name of the state in which it is located. If the state you entered is invalid or does not border the ocean, you will be prompted to enter a new state.
3. Based on your input harbor and state, the program generates a search url and attempts to navigate to the tides tab for your harbor of interest on www.usharbors.com. If your search url is invalid, you will be asked if you want to try again with a new state/harbor or quit the program. If your search url is valid, the program will grab the tide table html.

Next steps: Eventually it'll do something cool/helpful with the html (ex. let you run different commands to get high tide for today, low tide for the 17th of the month, etc.)
