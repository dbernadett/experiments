#!/usr/bin/env python3
a = [1,2,3,4]
b = map( lambda x:x*2, a)
print(dir(b))
print(b.next())
print(b)
for c in b:
	print(c)
