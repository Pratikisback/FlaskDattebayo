l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [x for x in l if x % 2 == 0]
print(a)

names = ["pratik", "vinay", "yash", "vishal"]
print(names[0])
print(names[-1])
names.append("mohan")
print(names)
alphabets = {"a": "apple", "b": "ball", "c": "cat"}
print(alphabets.values())

for i, j in alphabets.items():
    print(i, j)

print(alphabets["c"])

for keys, values in alphabets.items():
    if values == "cat":
        print(keys)

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
# for i in list2:
#     list1.append(i)
#
# print(list1)

# for i in list1:
#     list2.append(i)
#
# list2.sort()
# print(list2)

for i in list1:
    pass


l = []
stra= "Sumeet"
for i in stra:

    stra.split(",")
    l.append(i)

print(l)



















