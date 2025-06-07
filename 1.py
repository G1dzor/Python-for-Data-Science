import numpy as np

array=np.random.randint(1,101, size=(3,3))
print(array)

sum= np.sum(array)
print("\nСумма масиву ", sum)

max= np.max(array)
min= np.min(array)

max_i=np.argmax(array)
min_i=np.argmin(array)

print("Max val :", max, "  index: ", max_i)
print("Min val :", min, "  index: ", min_i)

sorted_arr=np.sort(array, axis=1)
print("\n Sorted: \n", sorted_arr)