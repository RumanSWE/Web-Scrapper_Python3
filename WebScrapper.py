#Job Web Scrapper
#Input Job Title and keywords and recivce matching URLS to Jobs
#search jobs with keyword input and location / add other options later
#BONUS: Send emails / quick apply with a CV which can be uploaded aswell

#Input Keywords (junior , developer , software (one word keep broad)
#loop through and collect all data (title,company,salary,description,email,datePosted)
#push to csv

#use CSV results to filter for key words AKA 'PHP' 
#BONUS: Send emails / quick apply with a CV which can be uploaded aswell

#https://www.linkedin.com/jobs/

import requests
from bs4 import BeautifulSoup
import re

#print('Enter Single Keyword For Job (Keep Broad such as "Developer"):')
#keyword = input()
#keyword = keyword.lower()

def getPages(page):
    URL = 'https://uk.indeed.com/jobs?q=junior&l=Manchester%2C+Greater+Manchester&start={page}'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup

c = getPages(40)
results = c.find_all("div", {"id": "searchCountPages"})[0].string.replace(",","")

print(results)
jobAmount = (re.findall(r'\d+', results)[1])
print(jobAmount);




#ResultsAmount = soup.find_all("div", {"id": "results-context-header__job-count"})[0].string
#print(ResultsAmount)


#'base-serp-page__content'
#for span in badges.span.find_all('span', recursive=False):
#    print span.attrs['title']
    

#print(results)


