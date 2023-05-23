# python-webscraper-emailer-tool
This tool uses Python to scrape data and send simple email reports scheduled through GitHub actions.
For this repo, it scrapes myprotein.com.sg to retrieve some text and sends an email every hour with the findings.

# How to use
1. Clone this repo
2. Under scrape.py, replace the url in line 17 with the link of your choice
3. Under scrape.py, replace the search criteria in line 19-20 based on the HTML div id, class, or tag name of your choice based on the selenium API (https://selenium-python.readthedocs.io/locating-elements.html)
4. Under scrape.py, replace the regex condition in line 23 to search for your desired text (use https://regex101.com/ to help)
5. Rename the myprotein_scraper.yml to anything you like, then change the cron schedule in line 5 to your desired schedule (https://crontab.guru/)
6. Set up the environment variables for the sender and receiver emails from the repo Settings > Secrets and Variables > Actions > New Repositoy Secret
7. For setting up the gmail details, follow this tutorial: https://www.youtube.com/watch?v=2OwLb-aaiBQ
