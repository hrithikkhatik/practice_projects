contacts = {
    "Rahul": 9876,
    "Aman": 1234
}
name = input("enter a name: ").title().strip()
if name in contacts:
    print(contacts[name])
else:
    print("Not found")