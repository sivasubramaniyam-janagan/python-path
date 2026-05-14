import numpy as np

mylist=[[1,2,3],
            [5,6,7],
            [7,9,0,]
            ]

array=np.array(mylist)

print(array[0])

print(array[:,0])
print(array[0:1,0:1])
print(array[0:2,0:2])
print(array[1:,1:])
