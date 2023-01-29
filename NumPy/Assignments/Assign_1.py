# 1. Create a null vector of size 10 but the fifth value which is 1.
import numpy as np
arr = np.zeros(10)
print("\nOriginal vector : ",arr)
arr[4] = 1
print('updated vector : ',arr)


# 2. Create a vector with values ranging from 10 to 49.
import numpy as np
arr = np.arange(10,50)
print('\nvector is :',arr)


# 3. Create a 3x3 matrix with values ranging from 0 to 8
import numpy as np
arr = np.arange(9)
print('\nvector :\n',arr)
mat = arr.reshape(3,3)
print('reshaping the vector :\n',mat)


# 4. Find indices of non-zero elements from [1,2,0,0,4,0]
import numpy as np
arr = np.array([1,2,0,0,4,0])
nz= arr.nonzero()
print('\nnon-zero elements :')
print(nz)


# 5. Create a 10x10 array with random values and find the minimum and maximum values.
import numpy as np
arr = np.random.random((10,10))
print('\noriginal array :\n',arr,"\nmin=",arr.min(),"and max=",arr.max())


# 6. Create a random vector of size 30 and find the mean value.
import numpy as np
arr = np.random.random(30)
print("\nvector : \n",arr,"\nmean value is", arr.mean())