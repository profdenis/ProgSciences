import matplotlib.pyplot as plt
import numpy as np

# x = [1, 2, 3, 4, 5]
# x = list(range(1, 6))
x = np.arange(1, 6)

# y = [1, 4, 9, 16, 25]
y = []
for i in x:
    y.append(i**2)

plt.figure(figsize=(5, 5))
plt.plot(x, y, ".r-")
plt.grid()
plt.show()