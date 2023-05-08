from heapq import heappop, heappush
import time
# start day, end day, rooms
reservations = [
	[3, 4, 1],
	[1, 3, 3],
	[2, 3, 1],
]
def max_nights_1(res):
	heap=[]
	for r in reservations:
		heappush(heap, (r[0],"s",r[1], r[2]))
	max_night = 0
	current = 0
	while len(heap) > 0:
		v =heappop(heap)
		if v[1] == "s":
			current+=v[3]
			max_night = max(max_night, current)
			heappush(heap, (v[2], "e", v[3]))
		if v[1] == "e":
			current-=v[2]
	return max_night
start = time.process_time()
print(max_nights_1(reservations))
print(time.process_time() - start)

def max_nights_2(res):
	events = []
	for r in res:
		events.append((r[0],"s",r[2]))
		events.append((r[1],"e",r[2]))
	events= sorted(events)
	print(events)
	max_night = 0
	current = 0
	for e in events:
		if e[1] == "s":
			current += e[2]
			max_night = max(max_night, current)
		if e[1] == "e":
			current -= e[2]
	return max_night
start = time.process_time()
print(max_nights_2(reservations))
print(time.process_time() - start)
