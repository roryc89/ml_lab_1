import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns

orders = pd.read_csv("data/Orders.csv")

orders.Profit = pd.to_numeric(
    orders.Profit.map(lambda x: re.sub("[\$\.,]", "", x))
)

orders.Sales = pd.to_numeric(
    orders.Sales.map(lambda x: re.sub("[\$\.,]", "", x))
)

orders["date"] = pd.to_datetime(orders["Order.Date"])

orders["month"] = orders.date.map(lambda d: d.month)
orders["year"] = orders.date.map(lambda d: d.year)

plt.figure(figsize=(32, 16))

orders.groupby(["year", "month"]).agg("count")["Row.ID"].barplot(
    kind="bar", subplots=True, orient="h"
)


counts = orders.groupby(["year", "month"]).agg("count")["Row.ID"]

counts.map(plt.hist)

g = sns.FacetGrid(counts)

g = g.map(plt.hist, "year")
# .unstack(1).plot(
#     kind="bar", subplots=True
# )

plt.show()
