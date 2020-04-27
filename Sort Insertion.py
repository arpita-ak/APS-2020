arr = [31,45,19,52,63,1,85] 

def insertionSort(arr): 
	for i in range(1, len(arr)): 

		key = arr[i] 
		j = i-1
		while j >= 0 and key < arr[j] : 
				arr[j + 1] = arr[j] 
				j -= 1
		arr[j + 1] = key 



insertionSort(arr) 
for i in range(len(arr)): 
	print ("% d" % arr[i]) 
