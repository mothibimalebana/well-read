import pandas as pd

# load data from csv
data = pd.read_csv("Books.csv")

# check if each book-title entry is unique
print(data['Book-Title'].is_unique)
