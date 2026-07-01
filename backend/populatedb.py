import pandas as pd

# load data from csv
data = pd.read_csv("Books.csv")
print(data.info())

# Normalize dataframes
Book = data['ISBN', 'Year-Of-Publication', 'Image-URL-S', 'Image-URL-M', 'Image-URL-L']
Author = data['Book-Author']
Publisher = data['Publisher']
