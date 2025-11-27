import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("sample-data-10mins.xlsx")
# print(data.head())
print(data["Product"], data["Boxes Shipped"], data["Date"])
plt.bar(data["Product"], data["Boxes Shipped"] )
plt.xlabel("Product")
plt.xticks(fontsize=7, rotation=45)
plt.ylabel("Boxes Shipped")
plt.show()
