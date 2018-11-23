# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from time import time
from random import randint

def swap(lst, i, j):
	temp = lst[i]
	lst[i] = lst[j]
	lst[j] = temp

def shuffle(lst):
	for i in range(len(lst)):
		j = randint(0, i)
		swap(lst, i, j)
		
def selection_sort(lst):
	for i in xrange(len(lst)):
		m = i
		for j in xrange(i, len(lst)):
			if lst[j] < lst[m]:
				m = j
		#lst[i], lst[m] = lst[m], lst[i]
		swap(lst, i, m)

def insertion_sort(lst):
	for i in xrange(1,len(lst)):
		j = i
		while j > 0 and lst[j] < lst[j-1]:
			swap(lst, j, j-1)
			j -= 1

def insertion_sort2(lst):
	for i in xrange(1,len(lst)):
		val = lst[i]
		j = i-1
		while j >= 0 and val < lst[j-1]:
			lst[j+1] = lst[j]
			j -= 1
		lst[j+1] = val

def bubble_sort(lst):
	for i in range(len(lst)-1,0,-1):
		for j in range(i):
			if lst[j] > lst[j+1]:
				lst[j], lst[j+1] = lst[j+1], lst[j]

def bubble_sort2(lst):
	swapped = False
	n = len(lst)
	while not swapped:
		swapped = False
		for i in range(n):
			if lst[i] < lst[i+1]:
				swap(lst, i, j)
				swapped = True
		n -= 1

def bubble_sort3(lst):
	n = len(lst)
	while n > 0:
		new_n = 0
		for i in range(1, n):
			if lst[i-1] > lst[i]:
				lst[i-1], lst[i] = lst[i], lst[i-1]
				new_n = i
		n = new_n

def test(lst, func):
	print(func.__name__)
	print('before:')
	print(lst)
	start = time()
	insertion_sort(lst)
	end = time()
	print('after:')
	print(lst)
	return end - start

if __name__ == '__main__':
	l = range(10)
	shuffle(l)
	funcs = [selection_sort]#, bubble_sort, insertion_sort, insertion_sort2]
	#funcs = [bubble_sort, bubble_sort2, bubble_sort3]
	for f in funcs:
		ls = l[:]
		t = test(ls, f)
		print('time to complete: '+str(t)+' seconds\n')