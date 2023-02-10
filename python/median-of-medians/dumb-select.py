#!/usr/bin/env python3

import math

def median_of_5(elements):
	if len(elements) > 5:
		print("median of 5 called with too many elements.")
		quit()
	for i in range(0, math.ceil(len(elements)/2)):
		min = i
		for j in range(i+1, len(elements)):
			if elements[j] < elements[min]:
				min = j
		elements[i], elements[min] = elements[min], elements[i]
	return elements[math.ceil(len(elements)/2) - 1]

def medians_of_5(elements):
	medians = []
	for i in range(0, len(elements), 5):
		end = min(i+5, len(elements))
		m = median_of_5(elements[i:end])		
		medians.append(m)
	return medians

def partition(elements, left, right, k):
	assert(0 <= left and left < right and 0 < len(elements) and right <= len(elements))
	print(f"{left}, {right}, {k}")
	elements[right-1], elements[k] = elements[k], elements[right-1]
	store_index = left
	for i in range(left, right-1):
		if elements[i] < elements[right-1]:
			elements[store_index], elements[i] = elements[i], elements[store_index]
			store_index += 1
	elements[right-1], elements[store_index] = elements[store_index], elements[right-1]
	return store_index

def select(elements, left, right, k):
	if left == right-1:
		return elements[left]
	pivotIndex = left #TODO: replace
	#pivotIndex = median_of_medians(elements[left:right])
	pivotIndex = partition(elements, left, right, pivotIndex)
	if k == pivotIndex:
		return(elements[k])
	elif (k < pivotIndex):
		return select(elements, left, pivotIndex, k)
	else:
		return select(elements, pivotIndex+1, right, k)


def median_of_medians(elements):
	meds = medians_of_5(elements.copy())
	return select(meds, 0, len(meds), len(meds)//2)

def main():
	items = [*range(1, 100)]
	
	
	
	

if __name__ == "__main__":
	main()
	median1 = median_of_5([1, 6, 8, 2, 0])
	median2 = median_of_5([1, 2, 3, 10, 5])
	print(median1 == 2)
	print(median2 == 3)
	print(median_of_5([1]) == 1)
	print(median_of_5([1,10]) in [1, 10])
	print(median_of_5([10, 2, 4]) == 4)
	print(median_of_5([-1, -3, 5, 0]) in [-1, 0])
	print(medians_of_5([1, 6, 8, 2, 0, 1, 2, 3, 10, 5, 10, 2, 4]))
	print([2, 3, 4])
	long_list = [1, 6, 8, 2, 0, 1, 2, 3, 10, 5, 10, 2, 4]
	print(long_list)
	#k = partition(long_list, 0, len(long_list), 3)
	#print(long_list)
	#long_list_2[k] = "*"
	#print(long_list)
	#print(k, long_list[k])
	sorted_list = []
	for i in range(0, 13):#len(long_list)):
	#for i in range(0, len(long_list)):
		ll = long_list.copy()
		print(ll)
		selected = select(ll, 0, len(ll), i)
		sorted_list.append(selected)
	print(long_list)
	print(sorted_list)
