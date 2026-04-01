import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("Sales.csv")
df["Postal Code"]=df["Postal Code"].astype("Int64")
df["Order Date"]=pd.to_datetime(df["Order Date"],errors='coerce')
df["Ship Date"]=pd.to_datetime(df["Ship Date"],errors='coerce')
df["Postal Code"]=df["Postal Code"].ffill()
#calculate total sales
total_sales=df["Sales"].sum()
print(f"Total Sales is : {total_sales}")
#calculate sales by region
region_sales=df.groupby("Region")["Sales"].sum()
print(f"The region wise Sales is : \n{region_sales}")
#calculate sales by category
category_sales=df.groupby("Category")["Sales"].sum()
print(f"The Sales by Category is : \n{category_sales}")
#calculate sales by sub-category
sub_category_sales=df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False)
print(f"The Sales of Sub_category is : \n{sub_category_sales}")
#Return Top 5 product by sales
Top_product=df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False).head(5)
print(f"The top 5 Products is : \n{Top_product}")
#sales by year - Extract year column from order date
df["Year"]=df["Order Date"].dt.year
yearly_sales=df.groupby("Year")["Sales"].sum()
print(f"The sales by year is : \n{yearly_sales}")
#bargraph
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()

category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

yearly_sales.plot(kind="line")
plt.title("Sales Trend Over Years")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.show()



