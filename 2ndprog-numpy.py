import numpy as np

sales_data = []
for i in range(9):
    b = int(input("Enter the sales data:"))
    sales_data.append(b)
c = np.array(sales_data)
print(c)
average_price = np.mean(sales_data)

print("Average price of all products sold in the past month:", average_price)
