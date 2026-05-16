import matplotlib.pyplot as plt
import numpy as np

categories=["action","adventure","fps","tps","platforming","indie"]
count=np.array([5,6,4,8,6,3])

plt.bar(categories,count,color="red")
plt.grid(axis="y")
plt.title("Games count")
plt.xlabel("Games")
plt.ylabel("Count")
plt.show()


