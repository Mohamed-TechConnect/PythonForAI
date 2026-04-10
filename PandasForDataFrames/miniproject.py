import pandas as pd
# Loading the data
df = pd.read_excel("C:/Users/DELL/Red9Sys/Sales.xlsx")


# Inspect the data
print("---- Mini Project ---")
#print(df)
#print("Head --- ", df.head())
#print("Info --- ", df.info())

# Handle the missing values

df["Sales"] = df["Sales"].fillna(0)

#print(df)

# Monthly sales
#group by monthly sales
#In jave define the variables like monthlySales --- using camelCase ---
#In Python we have to define variables like monthly_sales
product_sales = df.groupby("Product")["Sales"].sum()

#print(product_sales)

# Best product

best_product = product_sales.idxmax()

print("Best Product is ", best_product)




