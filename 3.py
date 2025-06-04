import numpy as np

arr=np.random.randint(1,226, size=(15,15))

sum_arr=np.sum(arr, axis=0)
print("Sum array:  \n", sum_arr)

dev=np.std(arr)
print("\nDeviation: ",dev)

t_arr=np.transpose(arr)

print ("Original array: \n",arr[:3, :3])
print("\nTransposed array: \n",t_arr[:3, :3])