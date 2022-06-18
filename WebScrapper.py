#Job Web Scrapper
#Input Job Title and keywords and recivce matching URLS to Jobs

#https://www.linkedin.com/jobs/

import requests

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

print(page.text)
