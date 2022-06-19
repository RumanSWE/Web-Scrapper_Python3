import pandas as pd


data = pd.read_csv("job.csv",  index_col=False)

df = pd.DataFrame(data, columns = ['1', 'title','company','summary','location','link'])

#print(df)
keywords = ["python","front end","frontend","remote", "react" "react native", "reactnative", "java", "javascript",
            "software", "developer","php"]

contain_values = df['summary']
print(len(contain_values))

#df = pd.read_csv("job.csv",  index_col=False).lower()

#filtered = df[df['title'].isin(keywords)]
# Save the filtered dataframe to a file
#filtered.to_csv("FilteredCSV.csv")


