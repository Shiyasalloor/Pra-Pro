import numpy as np
import time

#storing the initial time
start_time = time.time()

#creating 1000*1000 array
array = np.random.rand(1000, 1000)

#storing endtime
end_time = time.time()

#finding the array creation time
creation_time = end_time - start_time
print("Array creation time:", creation_time, "seconds")

#converting array to byte
array_bytes = array.tobytes()

#converting byte to array
recreated_array = np.frombuffer(array_bytes, dtype=array.dtype).reshape(array.shape)

#checking the the first array and recreated array are equal
print("Arrays match:", np.array_equal(array, recreated_array))
