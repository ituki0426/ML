import datetime
import numpy as np
import matplotlib.pyplot as plt
dt1 = datetime.datetime(year=2019, month=1, day=1, hour=12)
dt2 = datetime.datetime(year=2019, month=1, day=2, hour=12)
td = dt2 - dt1
print(td.total_seconds() / 1000)

day_1 = 86.4

ans = []
false = []
ans = {'x': np.array([1, 2, 3, 4, 5, 6]), 'y': np.array([2, 1, 5, 6, 3, 9])}
false = {'x': np.array([1, 2, 3, 4, 5, 6]), 'y': np.array([3, 2, 6, 7, 4, 10])}
plt.scatter(ans['x'], ans['y'], color="red")
plt.scatter(false['x'], false['y'], color="blue")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot")
plt.show()
