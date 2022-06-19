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
import pandas as pd



def getPages(page,keyword):
    URL = f'https://uk.indeed.com/jobs?q={keyword}&l=Manchester%2C+Greater+Manchester&start={page}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
    page = requests.get(URL,headers)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup

def transform(soup):
    divs = soup.find_all('div', class_ = 'job_seen_beacon')
    for items in divs:
        title = items.find('a').text.strip()
        company = items.find('span', class_='companyName').text.strip()
        try:
            salary = items.find('span',class_='attribute_snippet').text.strip()
        except:
            salary = ''
        summary = items.find('div',class_='job-snippet').text.strip() 
        location = items.find('div',class_='companyLocation').text.strip()
        link = items.find('a').get("href")
        indeed = "https://uk.indeed.com"
        link = f"{indeed}{link}"

        # description = items.find('div',class_='jobDescriptionText').text.strip() 
        job = {
            'title': title,
            'company': company,
            'salary': salary,
            'summary': summary,
            'location': location,
            'link': link,
        }
        jobList.append(job)

    return

print('Enter Single Keyword For Job (Keep Broad such as "Developer"):')
keyword = input()
keyword = keyword.lower()

jobList = []


for i in range(0,620,10):
    c = getPages(i,keyword)
    transform(c)

dataFrame = pd.DataFrame(jobList)
print(dataFrame.head())
dataFrame.to_csv('job.csv')

#results = c.find_all("div", {"id": "searchCountPages"})[0].string.replace(",","").strip()
#print(results)
#print(re.findall(r"(\d+) jobs", results)[0])


