import pandas as pd
import re
import matplotlib.pyplot as plt

orders = pd.read_csv("data/Orders.csv")
orders.info()

orders.Profit = pd.to_numeric(
    orders.Profit.map(lambda x: re.sub("[$.,]", "", x))
)

orders.Sales = pd.to_numeric(
    orders.Sales.map(lambda x: re.sub("[$.,]", "", x))
)

orders["date"] = pd.to_datetime(orders["Order.Date"]).dt.date

orders["month"] = orders.date.map(lambda d: d.month)
orders["year"] = orders.date.map(lambda d: d.year)

plt.figure(figsize=(32, 16))

sales_by_month = orders.groupby(["month"]).agg({"Quantity": "sum"})

plt.figure(figsize=(24, 12))
plt.bar(sales_by_month.index, sales_by_month.Quantity)
plt.xlabel("month")
plt.ylabel("sales")
plt.show()

for cat in orders.Category.unique():
    cat_orders = orders[orders.Category == cat]
    sales_by_month = cat_orders.groupby(["month"]).agg({"Quantity": "sum"})
    plt.figure(figsize=(24, 12))
    plt.bar(sales_by_month.index, sales_by_month.Quantity)
    plt.xlabel("month")
    plt.ylabel("sales of " + cat)
    plt.show()

returns = pd.read_csv("data/Returns.csv")

orders_and_returns = pd.merge(
    orders, returns, left_on="Order.ID", right_on="Order ID", how="left"
)

orders_and_returns.Returned = orders_and_returns.Returned == "Yes"


orders_and_returns[orders_and_returns.Returned].groupby(["year"]).agg(
    {"Profit": "sum"}
)

orders_and_returns["id"] = orders_and_returns["Row.ID"]
orders_and_returns.info()

customer_returns = (
    orders_and_returns[orders_and_returns.Returned]
    .groupby(["Customer.ID"])
    .agg({"id": "count"})
)

customer_returns[customer_returns.id > 1]

customer_returns[customer_returns.id > 5]

returns_by_region = (
    orders_and_returns[orders_and_returns.Returned]
    .groupby(["Region_y"])
    .agg({"id": "count"})
    .sort_values(by=["id"], ascending=False)
)

orders_and_returns["Ship.Date"] = pd.to_datetime(
    orders_and_returns["Ship.Date"]
)
orders_and_returns["Order.Date"] = pd.to_datetime(
    orders_and_returns["Order.Date"]
)

orders_and_returns["process_time"] = (
    orders_and_returns["Ship.Date"] - orders_and_returns["Order.Date"]
)

# returns_by_category = (
#     orders_and_returns[orders_and_returns.Returned]
#     .groupby(["Ca"])
#     .agg({"id": "count"})
#     .sort_values(by=["id"], ascending=False)
# )
#
# returns_by_category
