"""

Ask : Which product is selling the most
 # Which month has the highest revenue

 #Companies are making decisions based on the data -- using the AGGREGATION and GROUPING

 # Sales RAW data

 Month  Product     Sales

 JAN    Laptop      800
 JAN   Phone       500
 FEB    Laptop      900
 FEB    Phone       600

 total sales per month  - Which month has the highest revenue?
 total sales per product - Which product is selling the most?

 In python - we have groupby() --- group the data based on column then apply the aggregation





"""

# In this program my objective is to get the RAW sales data and process it to find the highest sales per product , per month and the show the output.

import pandas as pd

data = {
    "Month": ["JAN", "JAN", "JAN", "FEB", "FEB" ],
    "Product": ["Laptop", "Phone", "IPAD", "Laptop", "Phone"],
    "Sales": [800, 500, 300, 900, 600]
}

df = pd.DataFrame(data)

# print(df)

# how we can able to group it
result = df.groupby("Product")["Sales"].sum()

#print(result)

#Multi level grouping

print(df.groupby(["Month", "Product"])["Sales"].sum())

print(df.groupby(["Product", "Month"])["Sales"].sum())

# This is the exactly how dashboards and reports are generated in the IT companies using Python in the backend

#Real time use case
# Working more hours to cleaning the data -- Because the RAW Data is missing

# Sales column has some missing values
"""

Month   Product Sales
Jan     Lap     800
Jan     Mob     900
Feb     Iphone  Null

We can't calculate the totals with the missing data directly

How to detect the missing values?
df.isnull()

df["Sales"] =  df["Sales].fillna(0)

df.dropna()

MesssyData --> Clean Data --> Data Analytics

80%  of real world data work is ---> CLEANING the Data


"""

# Mini Project

#Manager wants monthly sales trend, Best selling Product, Clean Dataset

#  Raw Data --> Clean Data --> Group Data --> Insights --> Dashboards














