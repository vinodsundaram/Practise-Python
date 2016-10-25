a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for item in a:
	if item <5 :
		print (item)

less5 = list()
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for item in a:
	if item <5 :
		less5.append(item)
print(less5)

## oneline
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for item in [element for element in a	if element < 5]: print (item)

## input from user
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
param = int(input("ënter a number:"))
less = list()
for item in a:
	if item <param :
		less.append(item)
print(less)