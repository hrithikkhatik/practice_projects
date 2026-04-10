expenses = [100, 200, 50, 300]
average = sum(expenses) / len(expenses)
print(average)

max_val = expenses[0]
for i in expenses:
    if i > max_val:
        max_val = i
print(max_val)




