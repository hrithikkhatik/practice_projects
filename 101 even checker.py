nums = [10, 15, 20, 25, 30]
evens = []
for i in nums:
    if i % 2 == 0:
        evens.append(i)
#print(evens)

evens = [i for i in nums if i % 2 == 0]
print(evens)