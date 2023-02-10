#!/usr/bin/env python3

import sys

class PersonalValue:
	def __init__(self, name):
		self.name = name
	def __lt__(self, other):
		print(f"(1) {self.name} or (2) {other.name}")
		line = input()
		while(not line in ["1", "2"]):
			line = input()
		return True if line == "2" else False

def main():
	print("Hello World")
	personal_values = []
	with open("values.txt", "r") as f:
		for line in f:
			personal_values.append(PersonalValue(line[:-1]))
	personal_values.sort()
	for v in personal_values:
		print(v.name)

if __name__ == "__main__":
	main()
