list1 = [1, 5, 6, 10, 12, 18, 26, 29, 34, 36, 39, 48, 52, 61, 63, 68, 72, 75, 79, 81, 86, 88, 90, 92, 94, 98, 100]
new_list = []
for i in list1:
	if i < 90:
		new_list.append(i)
print(new_list)

new_list2 = []
number = int(input("Write a number "))
for x in list1:
	if x < number:
		new_list2.append(x)
print(new_list2)

print("I'm a good driver")

print("I am right")
