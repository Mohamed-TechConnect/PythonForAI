import pandas as pd

df = pd.read_excel("C:/Users/DELL/Red9Sys/Sales.xlsx")

print(df.head())

print(df.tail())

print(df.info()) #Information about Data Frames

# Filter above sales record is > 500

filtered = df[df["Sales"] > 500]

print(filtered)

# Sorting the values

sorted_df = df.sort_values(by="Sales", ascending=True)
print(sorted_df)

#selected columns
print("product and sales\n", df[["Product", "Sales"]])

