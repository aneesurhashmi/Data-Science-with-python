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

sale_1  = pd.Series({"Name":"Alif","Item purchased":"AAA","Price":31.22})
sale_2  = pd.Series({"Name":"Bay","Item purchased":"BBB","Price":21.5})
sale_3  = pd.Series({"Name":"Tay","Item purchased":"CCC","Price":50.90})

df = pd.DataFrame([sale_1, sale_2,sale_3], index= ["Shop 1","Shop 2", "Shop 1"])

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


# 