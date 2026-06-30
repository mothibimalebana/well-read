import pandas as pd

# load data from csv
data = pd.read_csv("Books.csv")

# Group by ISBN and get count of each feature
grouped_authors = data.groupby(['ISBN']).count().to_csv("group_by_isbn.csv")
