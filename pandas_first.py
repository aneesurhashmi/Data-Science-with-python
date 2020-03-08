import numpy as np
import pandas as pd

# print(pd.__version__)

games = ['CS', 'GTA', 'NFS', 'DELTA_FORCE', 'GHOST_RECON']
# Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.). It has to be remembered that unlike Python lists, a Series will always contain data of the same type
games_series = pd.Series(games)

culture = {'sindh': 'ajrak', 'balochista': 'dastaar',
           'KPK': 'P_chpl', 'punjab': 'khussay', 'AJK': 'gown'}
s = pd.Series(culture)
# print(s.values)
# print(s.index)

s1 = pd.Series(culture, index=['KPK', 'punjab', 'sindh', 'AJK'])
# print('s1: ', s1)
# KPK        P_chpl
# punjab    khussay
# sindh       ajrak
# AJK          gown

# ------------- Querying a Series ------------ #
# iloc for index
# print(s.iloc[3])
# loc for keys
# print(s.loc["KPK"])


file_content = """Reading information from files is a common and important operation in Python. In
this lecture we will discuss various options for reading files, and characterize
them based on simplicity and efficiency (mostly with regards to efficiency in
the use of space/memory, which is important when reading very large files).

In a nutshell, you should avoid the use of the .read() and .readlines() methods
and instead iterate over files (using a standard for loop or a for loop in a
comprehension).

The last section defines the parse_line function (available in the goody module)
and how to use it, making reading files that contain multi-type records (fields
of values) easy. One parameter binds to a tuple/list of function objects, each
specifying how to convert the field in its position (a substring of each line)
into a value of the appropriate type."""


# with open("test.txt", "w") as f:
#     # print(f.read())
#     f.write(file_content)

# with open("test.txt") as f:
#     i = 1
#     for line in f:
#         print(f"line number: {i}")
#         print(line.rstrip())
#         i+=1

# DataFrame data structure
# heart of pandas
# 2D series object with multiple column
# 2 axis labeled array

sale_1 = pd.Series({"Name": "Alif", "Item purchased": "AAA", "Price": 31.22})
sale_2 = pd.Series({"Name": "Bay", "Item purchased": "BBB", "Price": 21.5})
sale_3 = pd.Series({"Name": "Tay", "Item purchased": "CCC", "Price": 50.90})

df = pd.DataFrame([sale_1, sale_2, sale_3], index=[
                  "Shop 1", "Shop 2", "Shop 1"])

# we can querry a dataframe with loc and iloc attributes
# print(df.iloc[1])
# print(df.loc["Shop 1"])

# we can querry row and column intersection
# print(df.loc["Shop 1" , "Price"])
# print(df.loc["Shop 2"]["Item purchased"]) # this is expensive computationaly as compared to the first method (as it returns the copy of data frame instead of view into the data frame)

# We can transpose dataframe using T attribute (row label and column labels will be shuffled)
# print(df.T)

# sclicing in dataframe
# first parameter will be the row name/label range(: if we want full column). Second paramter will be the column label
# print(df.loc["Shop 2":,["Name", "Price"]])

# deleting a row: drop method (returs a copy of dataframe i.e original dataframe is not changed)
# print(df.drop("Shop 2"))

# deleting a column: drop method with optional parameters: columns --> column label to be deleted
# print(df.drop( columns = "Name"))
# or del keyword: this does not return a view, but has direct effects on dataframe
# del df["Name"]
# print(df)

# making copy of original dataframe: copy method
# df_copy = df.copy()
# print(df_copy)

# adding a new column
# df["Date"] = None
# print(df)

# ------------- Dataframe Indexing and Loading ------------- #
# Alert! If we manuplate a view into dataframe the base copy is also changed.
df_copy = df["Price"]
# print(df_copy)
# broadcast increment in price
df_copy += 35
# print(df_copy)
# price is also increased in df
# print(df)

# reading a file
# df = pd.read_csv("file_name.csv")
# print(df.columns)

# boolean masking: a one or 2 dimentional array, where each value is either True or False: Cells aligned with True values are included or considered
# df["Gold"] > 0 # here Gold is column label. The condition is being broadcast.
# this returns a boolean mask, i.e it is not applied to the dataframe yet.
# to apply it to dataframe, we use where method
# df_with_gold = df.where(df["Gold"] > 0)

# to drop rows with NA data: dropna method
# df_with_only_gold = df_with_gold.dropna()

# we can also use
# df_with_only_gold = df[df["Gold"]>0]

# making a column as index
# df.set_index(column name)
# multi level indexing
# df.set_index([column 1, column 2])
#

# =============================================================== #
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3],
                  index=['Store 1', 'Store 1', 'Store 2'])
# print(df)
# x = df.where(df["Cost"]> 3.00)
# print(df)
# print("df.index: ", df.index)
# print("index change")
# print(df)

purchase_4 = pd.Series({'Name': 'Hammad',
                        'Item Purchased': 'Chuchu Seed',
                        'Cost': 10.00})

df1 = pd.DataFrame([purchase_4],index=["Store 1"])
# print(df1)

# df = df.append(purchase_4)
# df["Location"] = df.index
# temp_indx = [i for i in df.index]
# print(temp_indx)
# temp_indx.append("Store 1")


df = df.append(df1)
df["Location"] = df.index
df = df.set_index("Location")
# print(df)

# df["Location"] = df.index
# print(df.set_index(["Location", "Name"]))
# df[-1] =
# print(df.set_index("Location"))
# df = df.set_index(["Location", "Name"])
# print(df)

# # print(x)
# # Your code hedfre



# Assignment 2 

### Question 1
# Which country has won the most gold medals in summer games?
# *This function should return a single string value.*

# def answer_one():
#     return df.where(df["Gold"] == max(df["Gold"])).dropna().index[0]
# answer_one()

# Question 2
# Which country had the biggest difference between their summer and winter gold medal counts?
# This function should return a single string value.
 
# def answer_two():
#     diff  = df["Total"] - df["Total.1"]
#     diff_value = max([min(diff)*-1, max(diff)])
#     return diff.where(diff == diff_value).dropna().index[0]
# answer_two()

# Question 3

# Which country has the biggest difference between their summer gold medal counts and winter gold medal counts relative to their total gold medal count?

# Summer Gold−Winter GoldTotal Gold
# Summer Gold−Winter GoldTotal Gold

# Only include countries that have won at least 1 gold in both summer and winter.

# This function should return a single string value.


# def answer_three():
#     df1 = df.copy()
#     df1 = df1.where((df1["Gold.1"] > 0) &  (df1["Gold"] > 0 )).dropna()
#     diff  = (df1["Total"] - df1["Total.1"]) / df1["Combined total"]
#     diff_value = max([min(diff)*-1, max(diff)])
#     return diff.where(diff == diff_value).dropna().index[0]
# answer_three()


# Question 4

# Write a function that creates a Series called "Points" which is a weighted value where each gold medal (Gold.2) counts for 3 points, silver medals (Silver.2) for 2 points, and bronze medals (Bronze.2) for 1 point. The function should return only the column (a Series object) which you created, with the country names as indices.

# This function should return a Series named Points of length 146

# def answer_four():
#     scores = df["Gold.2"] * 3 + df["Silver.2"] * 2 + df["Bronze.2"]
#     Points = pd.Series(scores, index = df.index)
#     return Points
# answer_four()

# ====================== tutorials ====================== #

df = pd.read_csv("sample_data.csv")
# print(df)

rows, shape = df.shape
# print(rows, shape)
# print(df.head())
# print(df.tail(2))
# print(df.columns)
# print(df[2:5]) print row 2 to 5 (5 not included)