#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Write a program to perform bubble sort on a list
# list- 34,56,71,3,19,5

def Solution(arr):
	n = len(arr)
	# optimize code, so if the array is already sorted, it doesn't need
	# to go through the entire process
	swapped = False
	# Traverse through all array elements
	for i in range(n-1):
		# range(n) also work but outer loop will
		# repeat one time more than needed.
		# Last i elements are already in place
		for j in range(0, n-i-1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if arr[j] > arr[j + 1]:
				swapped = True
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		
		if not swapped:
			# if we haven't needed to make a single swap, we
			# can just exit the main loop.
			return