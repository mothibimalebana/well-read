import pandas as pd

# load data from csv
data = pd.read_csv("Books.csv")

# check if each isbn entry is unique
print(data['ISBN'].is_unique)

# load first 20 rows into a csv file
create_first_20_csv = data.head(20).to_csv("first_20.csv", index=False)