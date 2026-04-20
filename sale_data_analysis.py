import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("SaleData (1).xlsx")
arr = np.array(data)
# print(arr)

arr = arr[:-2]
# print(arr)

#Manager with the most sales
print("Max sale amt", np.max(arr[:, -1]))
print("Manager Name: ", arr[np.argmax(arr[:, -1]), 2])
# print("\n")

sum_arr = []
managers = ["Martha", "Douglas", "Hermann", "Timothy"]
martha = arr[arr[:, 2] == "Martha"]
sum_arr.append(np.sum(martha[:, -1]))

douglas = arr[arr[:, 2] == "Douglas"]
sum_arr.append(np.sum(douglas[:, -1]))

hermann = arr[arr[:, 2] == "Hermann"]
sum_arr.append(np.sum(hermann[:, -1]))

timothy = arr[arr[:, 2] == "Timothy"]
sum_arr.append(np.sum(timothy[:, -1]))
# print(sum_arr)

# Managers vs Sale amt #
plt.pie(x=sum_arr, labels=sum_arr)
plt.title("Managers vs Sale amt")
plt.legend(managers)
plt.show()

# Sale amt vs Region #
plt.bar(arr[:, 1], arr[:, -1])
plt.title("Sale amt vs Region")
plt.show()

# Sale amt vs Salesman #
plt.bar(arr[:, 3], arr[:, -1], color="lightgreen")
plt.title("Sale amt vs Salesman")
plt.show()

# Sale amt vs Item #
plt.bar(arr[:, 4], arr[:, -1], color="lightblue")
plt.title("Sale amt vs Item")
plt.show()
