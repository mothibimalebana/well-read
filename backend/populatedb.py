import pandas as pd

# load data from csv
data = pd.read_csv("Books.csv")

# Group by authors and get count of each feature
grouped_authors = data.groupby(['Book-Author']).count().to_csv("group_by_authors.csv")
