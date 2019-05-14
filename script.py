import pandas as pd
import re

orders = pd.read_csv("data/Orders.csv")

orders.info()

orders.Profit.head()

orders.Profit = pd.to_numeric(
    orders.Profit.map(lambda x: re.sub("[\$\.,]", "", x))
)

orders.Sales = pd.to_numeric(
    orders.Sales.map(lambda x: re.sub("[\$\.,]", "", x))
)
