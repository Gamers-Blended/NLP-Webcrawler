import pandas as pd

# scrap data with the crawler first to generate the news.csv file
df=pd.read_csv("news.csv",sep=",")

# remove special characters in header column
df['header'] = df['header'].replace(':', '', regex=True)
df['header'] = df['header'].replace('/', '', regex=True)
df['header'] = df['header'].replace('?', '', regex=False)

# create txt file in output folder
for index in range(len(df)):
   try:
     with open('output/' + df["header"][index] +  '.txt', 'w', encoding="utf-8") as output:
        output.write(df["word"][index])
   except:
      pass