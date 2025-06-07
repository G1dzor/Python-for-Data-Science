import numpy as np

arr=np.random.randint(-100,101, size=200)
print(arr)

mask = arr<0
arr[mask]=0
print("\n\n Modified: \n",arr)

mean_value=np.mean(arr)
print("Mean:  ",mean_value)