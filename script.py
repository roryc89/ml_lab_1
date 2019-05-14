import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns

orders = pd.read_csv("data/Orders.csv")
orders.info()
orders.Profit = pd.to_numeric(
    orders.Profit.map(lambda x: re.sub("[\$\.,]", "", x))
)

orders.Sales = pd.to_numeric(
    orders.Sales.map(lambda x: re.sub("[\$\.,]", "", x))
)

orders["date"] = pd.to_datetime(orders["Order.Date"]).dt.date

orders["month"] = orders.date.map(lambda d: d.month)
orders["year"] = orders.date.map(lambda d: d.year)

plt.figure(figsize=(32, 16))

# orders.groupby(["year", "month"]).agg("count")["Row.ID"].barplot(
#     kind="bar", subplots=True, orient="h"
# )
sales_by_month = orders.groupby(["month"]).agg({"Quantity": "sum"})


plt.figure(figsize=(24, 12))
plt.bar(sales_by_month.index, sales_by_month["Row.ID"])
plt.xlabel("month")
plt.ylabel("sales")
plt.show()

sales_by_category = orders.groupby(["Category", "month"]).agg(
    {"Row.ID": "count"}
)
# tips = sns.load_dataset("tips")
# g = sns.FacetGrid(tips, col="time", row="smoker")
for
orders[orders.Category == "Furniture"]


g = sns.FacetGrid(orders, col="Category", row="month")
g = g.map(plt.bar, "Quantity")
# counts.map(plt.hist)

# g = sns.FacetGrid(counts)

# g = g.map(plt.hist, "year")
# .unstack(1).plot(
#     kind="bar", subplots=True
# )

plt.show()
