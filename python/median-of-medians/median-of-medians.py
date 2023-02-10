#!/usr/bin/env python3

import math
import random

def main():
	items = [*range(1, 100)]

# def partition5(elements, left, right)
#     for i in range(left + 1, right)
#         j := i
#         while j > left and list[j−1] > list[j] do
#             swap list[j−1] and list[j]
#             j := j − 1
#         i :=  i + 1
            
#     return floor((left + right) / 2)

partition5_called = 0
def partition5(elements, left, right):
	global partition5_called
	partition5_called += 1
	elements[left:right] = sorted(elements[left:right])
	return math.floor((left+right)/2)

def gather_pivots(elements, left, right):
	if right-left <= 5:
		#print("less than 5")
		return partition5(elements, left, right)
	for i in range(left, right, 5):
		subright = i + 5
		if subright > right:
			subright = right
		median5 = partition5(elements, i, subright)
		elements[median5], elements[left + math.floor((i-left)//5)] = elements[left + math.floor((i-left)//5)], elements[median5]
	mid = (right - left) // 10 + left
	return mid
	#return select(elements, left, left + floor((right - left) / 5), mid)

def pivot(elements, left, right, depth):
	mid = gather_pivots(elements, left, right)
	if right-left <= 5:
		return mid
	return select(elements, left, left + math.ceil((right - left) / 5), mid, depth+1)

def select(elements, left, right, n, depth = 0, pivot_f = pivot):
	i = 0
	while(True):
		assert(right > left), f"{elements}"
		#print(f"{i}.{depth}: {elements[left:right]}")
		i += 1
		if left == right-1:
			if depth == 0:
				print(i)
			return left
		pivotIndex = pivot_f(elements, left, right, depth)
		#print(f"{i}.{depth}  pi:{pivotIndex}, pv:{elements[pivotIndex]}")
		pivotIndex = partition(elements, left, right, pivotIndex, n)
		if n == pivotIndex:
			if depth == 0:
				print(i)
			return n
		elif n < pivotIndex:
			right = pivotIndex
		else:
			left = pivotIndex + 1
comparisons_made = 0
def partition(elements, left, right, pivotIndex, n):
	global comparisons_made
	comparisons_made += right-left
	assert(n >= left and right > n and pivotIndex >= left and pivotIndex < right), f"{left}, {right}, {pivotIndex}, {n}"
	pivotValue = elements[pivotIndex]
	#print(f"pv {pivotValue}")
	less = list(filter(lambda x: x < pivotValue, elements[left:right]))
	equal = list(filter(lambda x: x == pivotValue, elements[left:right]))
	more = list(filter(lambda x: x > pivotValue, elements[left:right]))
	elements[left:right] = less + equal + more
	if n < len(less) + left:
		return len(less) + left
	elif n <= len(less) + len(equal) + left - 1:
		return n
	else:
		return len(less) + len(equal) + left - 1

def reset():
	global partition5_called
	global comparisons_made
	print(f"partition5_called: {partition5_called}")
	print(f"comparisons_made: {comparisons_made}")
	partition5_called = 0
	comparisons_made = 0

if __name__ == "__main__":
	s0 = []
	s1 = [1]
	s2 = [8,7]
	s3 = [8,5,9]
	s4 = [8,5,9,10]
	s5 = [8,5,9,5,-1]
	s6 = [-3, 15, 1] + s5.copy() + [1, 0]
	e1 = s6.copy()
	print(e1)
	print(partition5(e1, 3, 8))
	print(e1)
	e2 = s6.copy()
	print(e2)
	e2_p = partition(e2, 2, len(e2)-1, 5, 5)
	print(e2_p)
	print(e2)
	#print(e2[e2_p] ==)
	print("Gather Pivots Test:")
	e3 = s5 + s5 + s5 + s3
	print(e3)
	gp = gather_pivots(e3, 5, len(e3))
	print(gp)
	print(e3)
	print("Select Test")
	size = 40
	print("Size", size)
	index = 2
	e4 = [*range(0, size)]
	seed = 2
	random.seed(seed)
	random.shuffle(e4)
	#print(e4)
	reset()
	i = select(e4, 0, len(e4), index, 0, lambda e, left, right, depth: left)
	print(f"i: {i}, v:{e4[i]}")
	reset()
	print("Select with median-of-medians")
	e4 = [*range(0, size)]
	random.seed(seed)
	random.shuffle(e4)
	#print(e4)
	i = select(e4, 0, len(e4), index, 0)
	print(f"i: {i}, v:{e4[i]}")
	#print(e4)
	print(f"VS {size**2} or {size*math.log(size,2)}")
	reset()



	

