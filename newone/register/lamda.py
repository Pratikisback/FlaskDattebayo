# a  = [x for x in range(1,1001) if x%8 == 0]
# print(a)
import pprint

# a = [x for x in range(1,1001) if "6" in str(x)]
# print(a)


# string2 = string1.split(" ")
# print(string2)
# lista = [x for x in string1]
# b = ''.join(lista)
# print(b)
#
# list1 = "".join([x for x in string1])
# list2 = "".join([x for x in string1 if x not in ["a","e","i","o","u"]])
# print(list2)
# print(list1)


# lis = ["Pratik", "Ram","amit", "Yash", "Himesh"]
# a = [x for x in lis if len(x) > 4]
# print(a)
# string1 = "Hello  I am Kraken I love to eat humans"
#
# d = {x: len(x) for x in string1.split()}
# # print(d)
#
# l = [x for x in string1.split() if "k" not in x]
# # print(l)
#
# k = [x for x in string1.split() if len(x) < 5]
# # print(k)
#
#
# p = [n for n in range(1,10)]
# print(p)

# lp = [x for x in range(1,1001) if x%7 == 0]
# print(lp)
#
# ku = [x for x in range(1,1001) if "3" in str(x)]
# print(ku)
#
# bankai = "bankai katen kyokotsu karamatsu shinju"
# po = len([x for x in bankai if x == " "])
# print(po)

# d = "Yellow yalks like yelling and yawning and yesterday they yoddled  while eating yuky yams"
# lk= [x for x in d if x in  ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]]
# print(lk)

# nums  = range(1, 1001)
# q8_answer = {num:max([divisor for divisor in range(1,10) if num % divisor == 0]) for num in nums}
# print(q8_answer)


# a=["hi", 4, 8.99, "apple" ,('t,b','n')]
# z = [(x, a.index(x)) for x in a]
# print(z)

# a = [1,2,3,4]
# b = [2,3,4,5]
# c = []
# for x in a:
#     for y in b:
#         if x == y:
#             print(x)


# li = [x for x in a for y in b if x == y]
# print(li)


# li = [x for x in stringo.split() if x.isdecimal()]   #iterable.isdecimal() returns the actual digit, remember you are an idiot
# print(li)

# li = [ x for x in range(1, 21) if x%2 == 0 ]
# print(li)
#
# li = range(1,21)
# for x in li:
#     if x%2 == 0:
#         print("even")
#     else:
#         print("odd")

# l1=['even' if i%2==0 else 'odd' for i in range(1,21)]
# print(l1)

# a = [1,2,3,4,5,6,7,8,9]
# b = [2,7,1,12]
# ls = [(x,y) for x in a for y in b if x==y]
# print(ls)


# stringo = "In 1984 there were 13 instances of a protest with over 1000 people attending"
# li = [x for x in stringo.split() if len(x)< 4]
# print(li)

#
# li = [(x, y) for x in range(1,101) for y in range(9, 2, -1) if x % y == 0 ]
# print(li)
# #
# ll = [1, 2, 3, 4, 5, 6]
# a = max(ll)
# print(a)

# for x in range(1,1001):
#
#     for y in range(9,2,-1):
#         if x%y == 0:
#             print(x,y)
#             break

# print("New Change")


# dictio = {"INS": 67, "ST": 69, "AI":39, "WS": 63, "GP":45}
# for k,v in dictio.items():
#     # print(v)
#     pass
#
#
# a = "     git status     "
# b = a.replace(" ", "")
# print(b)
#
# c = a.strip(" ")
# print(c)
# #
# matrix = [[2,1,5],
#           [5,99,0],
#           [33,2,4]]
#
# z = [max(x) for x in matrix ]
# print(z)


from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["PracticeDB"]
collection = db["Restaurents"]

# a = collection.find()
# pprint.pprint(list(a))

# b = collection.find({}, {"restaurant_id": 1, "name": 1, "borough": 1, "cuisine": 1})
# pprint.pprint(list(b))

# c = collection.find({}, {"restaurant_id": 1, "name": 1, "borough": 1, "cuisine": 1, "_id": 0})
# pprint.pprint(list(c))

# d = collection.find({}, {"restaurant_id": 1, "name": 1, "borough": 1, "cuisine": 1, "address.zipcode": 1, "_id": 0})
# pprint.pprint(list(d))

# e = collection.find({"borough": "Bronx"})
# pprint.pprint(list(e))

# f = collection.find({"borough": "Bronx"}).limit(5)
# pprint.pprint(list(f))

# g = collection.find({"borough": "Bronx"}).skip(5).limit(5)
# pprint.pprint(list(g))

# h = collection.find({"grades":{"$elemMatch":{"score": {"$gt": 90}}}})
# pprint.pprint(list(h))

# i = collection.find({"$and":[{"grades":{"$elemMatch":{"score": {"$gt": 80}}}}, {"grades": {"$elemMatch":{"score":{"$lt": 100}}}}]})
# pprint.pprint(list(i))

# j = collection.find({"address.coord": {"$lt": -95.754168}})
# pprint.pprint(list(j))

# k = collection.find({"cuisine": {"$ne": "American"}, "grades.score": {"$gt": 70}, "address.coord": {"$lt": -65.754168}})
# pprint.pprint(list(k))


# Could not solve
# l = db.Restaurents.find({"cuisine": {"$ne": "American"}, "grades.grade": "A", "borough":{"$ne": "Brooklyn"}})
# pprint.pprint(list(l))

# m = collection.find({"name": {"$regex": "^Wil"}}, {"restaurant_id": 1, "borough":1, "cuisine": 1, "name": 1})
# pprint.pprint(list(m))

# n = collection.find({"name": {"$regex": "ces$"}}, {"restaurant_id": 1, "borough":1, "cuisine": 1, "name": 1})
# pprint.pprint(list(n))


# Could not solve
# o = collection.find({"name": {"$regex": "/.*Reg.*/"}}, {"restaurant_id": 1, "borough":1, "cuisine": 1, "name": 1})
# pprint.pprint(list(o))

# p = collection.find({"borough":"Bronx", "$or":[{"cuisine":"American"}, {"cuisine": "Chinese"}]})
# pprint.pprint(list(p))

# q = collection.find({"borough": {"$nin":["Staten Island", "Bronx", "Queens", "Brooklyn"]}}, {"name": 1, "restaurant_id": 1, "borough": 1, "cuisine": 1})
# pprint.pprint(list(q))

# r = collection.find({"grades":{"$elemMatch":{"score": {"$lt": 10}}}},{"restaurant_id": 1, "name": 1, "borough": 1, "cuisine": 1, "grades.score":1})
# pprint.pprint(list(r))


# Not sure if written correctly
# s = collection.find({"$or": [{"name":{"$ne": {"$regex": "^Wil"}}}, {"$and":[{"cuisine":{"$ne": "Chinese"}}, {"cuisene": {"$ne":"Chinese"}}]}]},
#                     {"restaurant_id":1, "name": 1, "borough": 1,"cuisine":1})
# pprint.pprint(list(s))


# a= collection.find({"$or":[{"weight": {"$gt": 160}}, {"height":{"$gt": 50}}]})
# print(list(a))

# b = collection.find()
# # pprint.pprint(list(b))
#
# c = collection.find({"name": "Pratik"})
# # pprint.pprint(list(c))
#
# d = collection.find({}, {"name": 1, "height": 1, "_id": 0})
# # pprint.pprint(list(d))
#
# e = collection.find({"height": 169}, {"name": 1, "_id": 0} )
# # pprint.pprint(list(e))
#
# #limit() can be used as head() used in pandas
# f = collection.find({"name": "Pratik"}, {"height": 1, "weight": 1, "_id": 0, "name": 1}).limit(2)
# # pprint.pprint(list(f))
#
# g = collection.find({"height": {"$gt": 169}})
# # pprint.pprint(list(g))
#
# #skip() is used in mongo to skip documents as per the need to read
# f = collection.find({"weight": {"$gt": 65}}).skip(3).limit(3)
# # pprint.pprint(list(f))
#
# h = collection.find({"$and":[{"height": {"$gt": 165}}, {"height": {"$lt": 170}}]})
# # pprint.pprint(list(h))
#
# i = collection.find_one({"name": "Vinay"})
# # pprint.pprint(i)


# print("Started again")

# i = 1
# while i<=5:
#     i +=1
#     print("Python")
#

# i = 1
# j = 1
# while i <= 5:
#     i = i +1
#     print("python")
#     while j <= 5:
#         j = j + 1
#         print("evolves")


l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in range(len(l)):
#     for j in range(len(l)):
#         if i==j:
#            pass # print(l[i][j],end="")
#     # print()
#
#
a = [l[i][i] for i in range(len(l))]
# print(a)
#
#


# for x in range(0,len(m)):
#     for y in range(0,len(m)):
#         if x == y:
#             print(m[x][y])
# for i in range(len(m)):
#      for j in range(len(m)):
#
#           # print(i , j)
#
#           if i+j == 2:
#                print(m[i][j])


# m = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# no = [m[i][j] for i in range(len(m)) for j in range(len(m)) if i+j == 2]
# print(no)
#
# s = [1, 2, 3, 4]
# b = s[0]
# c = s[3]
# s[0] = c
# s[3] = b
# print(s)


# overs = [5, 7, 2, 3, 5] swap 7 and 2 with each other
# overs = [5, 7, 2, 3, 5]
# print(overs)
# x = overs.pop(1)
# y = overs.pop(1)
# print(overs)
# k = overs.insert(1,x)
# l = overs.insert(1,y)
# print(overs)

# components = ["thread", "ropes", "clothes", "WaterCans", "Matchbox"]
# count = 0
# for i in components:
#     # print(i)
#     count = count + 1
#
# print(count)
#     # if i:
#     # count +=1
#     # print(count)


# a = list(string1)
# print(a)
# b = a[:len(a)//2]
# c = a[len(a)//2:]
# d = a[len(a)::-1]
# e = d[len(d)//2:]
# print(e)
# print(d)
# print(b)
# print(c)
# if b == c:
#      print("It is a symmetrical word")
# else:
#      print("Not symmetrical")


# string1 = "toltol"
#
# a = list(string1)
# print(a)
# b = a[len(a) // 2:]
# print(b)
# c = a[:len(a) // 2]
# print(c)
# d = c[::-1]
# print(d)
#
# if b == c and c==d:
#     print("Palindrome")
#
# elif b == c:
#     print("Symmetrical string")
#
# elif b != c:
#     print("Asymmetrical")
#




#
# a = "My magic is never giving up"
# b = list(a.split(" "))
# print(b[::-1])


# a = "And that's how gods are created"
# l = a.replace(" ", "")
# print(a)
# print(l)
# n = (list(l))
# n.remove(n[6])
# print(str(n))
# j = "".join(n)
# print(j)

#
# p = [1,2,3,4]
# b = [(i, i**2) for i in p]
# print(b)
#

# a = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
# b = list(a.keys())
# b.sort()
# k = {i : a[i] for i in a }
# print(k)

a = {}
a[2] = 90
a[3] = 80
a[6] = 87
a[1] = 99

print(a)
b = (list(a.keys()))
b.sort()
print(b)
j = {i: a[i] for i in b}
print(j)







