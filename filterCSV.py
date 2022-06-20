import pandas as pd


data = pd.read_csv("job.csv",  index_col=False)

df = pd.DataFrame(data, columns = ['number', 'title','company','summary','location','link'])


keywords = ["python","front end","frontend","remote","react","react native","reactnative","java","junior","javascript","software","developer","php","C#","matlab","back end","backend","swift","java script","mobile"]
#List of keyword to filter the general job search critera (add as many as possible)
banned = ["senior","ux","lead","manager","principal","director","mid"]

summary = df['summary'].str.lower()
title = df['title'].str.lower()
company =df['company']
location =df['location']
link = df['link']

filteredArr=[]
bannedArr=[]
jobList = []

for i in range(len(summary)):
    if any(word in summary[i] for word in keywords):
        filteredArr.append(i)
    if any(word in title[i] for word in keywords):
        filteredArr.append(i)
    if any(word in title[i] for word in banned):
        bannedArr.append(i)



#print(bannedArr)
filteredArr = list(set(filteredArr))
filteredArr.sort()

filteredArr = [fruit for fruit in filteredArr if fruit not in bannedArr]

print(filteredArr)

for i in range(len(filteredArr)):  
    job = {
        'title': title[filteredArr[i]],
        'company': company[filteredArr[i]],
        'summary': summary[filteredArr[i]],
        'location': location[filteredArr[i]],
        'link': link[filteredArr[i]],
    }
    jobList.append(job)

dataFrame = pd.DataFrame(jobList)
#print(dataFrame.head())
dataFrame.to_csv('filteredCSV.csv')

