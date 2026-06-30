import pandas as pd

# load data from csv
data = pd.read_csv("Books.csv")

# check if each isbn entry is unique
print(data['Book-Title'].is_unique)
