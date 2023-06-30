# a  = [x for x in range(1,1001) if x%8 == 0]
# print(a)
import copy
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
#
# a = {}
# a[2] = 90
# a[3] = 80
# a[6] = 87
# a[1] = 99
#
# print(a)
# b = (list(a.keys()))
# b.sort()
# print(b)
# j = {i: a[i] for i in b}
# print(j.keys())


dict1 = {}
dict1[1] = "Pratik"
dict1[2] = "Vinay"
dict1[3] = "Aditya"
dict1[4] = "Yash"
dict1[5] = "Faiz"
dict1[6] = "Saurabh"

#
# for i, k in dict1.items():
#
#     print(i,k)
# print("This is for a normal dict")

# from collections import OrderedDict
#
# Odict1 = OrderedDict()
# Odict1[1] = "Pratik"
# Odict1[2] = "Vinay"
# Odict1[3] = "Aditya"
# Odict1[4] = "Yash"
# Odict1[5] = "Faiz"
# Odict1[6] = "Saurabh"
#
# for i, k in Odict1.items():
#     Odict1[5] = "Ritvik"
#     print(i,k)
#
# b = Odict1.pop(3)
# print(Odict1)
#
# Odict1[2] = "Nick"
# l = {i: k for i,k in Odict1.items()}
# print(l)


# m = [[1,2,3,4],[4,5,6,9],[7,8,9,8]]
# for i in range(0,len(m)):
#
#     for j in range(0, len(m)):
#         if i+j == 3:
#             print(m[i][j])

# for i in range(len(l)):

#     for j in range(1, len(l)):
#         if l[j] == target - l[i]:
#
#             print(i,j)
# l = [3,2,4]
# target = 7
# def twosum(l, target):
#     start, end, total = 0, len(l) - 1, 0
#     while (start < end):
#
#         total += l[start] + l[end]
#         if total> target:
#             end -= 1print(names.count("Mohan"))
#         elif total< target:
#             start += 1
#         elif total == target:
#             return [start, end]
#         total=0
#
# print(twosum(l, target))

# l = [2, 7, 11, 13]
# target = 9

# def twosum(l, target):
#     seen = {}
#     for index, num in enumerate(l):
#         diff = target - num
#         if diff in seen:
#             return(seen[diff], index)
#         elif num not in seen:
#             seen[num] = index
#
# print(twosum([2,7,11,13], 9))


# x = [x for x in range(2000, 3201) if (x%7 ==0) and (x%5 == 0)]
# print(x)
# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return x *factorial(x-1)
# print(factorial(8))
#
#

# x = 8
# b =1
# for i in range(1, x+1):
#     b *= i
#
# print(b)


# n = int(input("Enter a number:  "))
# k = dict()
# for i in range(1,n+1):
#     k[i] =i*i
# print(k)

# li = [1,2,3,'a','b','c']
# for i in li:
#     if 2 in li:
#         print("yes")
# print("yes")


# name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
# animal = ['Cat', 'Dog', 'Fish', 'Goat']
# age = [1, 2, 2, 6]

# zipped_list = zip(name, animal, age)
#
# for i in zipped_list:
#     print(i)
#
# print(name+animal+age)
# name.extend(["Cruger"])
#
# n = ["hello", "hi", "thanks"]
# name.extend(n)
# for i in name:
#     if i == "Snowball":
#         del i
# print(name)
#


name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
animal = ['Cat', 'Dog', 'Fish', 'Goat']
age = [1, 2, 2, 6]
#
# for i in name:
#     del name[2]
# print(name)

k = [1, 2, 3, 4, 5, 7, 8, 3, 1, 4, 6, 7, 3, 2]
# v = []
# n =[v.append(x) for x in k if x not in v]
# print(v)
#
# print(k.index(2))
# print(name.index("Bubbles"))
#
# print(k.clear())

names = ["Pratik", "Vinay", "Vishal", "Mohan", "Yash", "Pratik", "Vinay", "Vishal", "Mohan"]
# print(names.count("Mohan"))
# j = []
# ab = [j.append(x) for x in names if x not in j]
# print(j)

# counter = 0
# for i in names:
#     if names.count(i) > 1:
#         names.remove(i)
#         counter += 1
# print(names)
# print(counter)

# for i, j in enumerate(names):
#     if j == "Pratik":
#         print(i, j)
# #

# namess= ["Pratik", "Vinay", "Vishal", "Mohan", "Yash", "Pratik", "Vinay", "Vishal", "Mohan"]
# namess.pop(5)
# names.remove("Pratik")
# print(namess)
# print(namess)
# friends = names.copy()
# print(friends)
#
# for i in friends:
#     if "M" in i:
#         friends.remove(i)
# print(friends)
from copy import deepcopy

# round1 = [
#     ['Arnold', 'Sylvester', 'Jean Claude'],
#     ['Buttercup', 'Bubbles', 'Blossom']
#
# ]
# round2 = round1.copy()
# round3 = copy.deepcopy(round1)
# print(round2)
# print(round3)

# li = [1,2,3,4,5,6,7,8,9]
# print(5 in li)
# print(5 not in li)

alphabet = ['a', 'b', 'c']
integers = [1, 2, 3]

# k = lis(zip(alphabet, integers))
# print(k)
# alphabet.insert(2, "I am 2")
# print(alphabet)
# for i in alphabet:
#     print(i)
#
# print(alphabet[1])
#
# test_list = [[5, 8, 9], [2, 0, 9], [5, 4, 2], [2, 3, 9]]
# z = {test_list[0][x] : test_list[x] for x in range(len(test_list)-1)}
# print(z)


#
#
# count = 0
# list1 = ['abc', 'xyz', 'aba', '1221']
# for word in list1:
#     if (len(word)> 2) and word[0] == word[-1]:
#         count +=1
#         print(word)
# print(count)

# def last(n): return n[-1]
#
# def sort_list_last(tuples):
#   return sorted(tuples, key=last)
#
# print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

#
# al = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# al.sort(key = lambda x: x[1])
# print(al)

# nl = [1,2,3,4,5,6,6,7,8,3,2]
# b = []
# for i in nl:
#     if i not in b:
#         b.append(i)
# print(b)


# lower_value = 2
# upper_value = 100
# for number in range(lower_value, upper_value):
#   if number > 1:
#     for i in range(2, number):
#       if (number%i) == 0:
#         break
#     else:
#       print(number)
#


# def generatorr():
#   for i in range(5):
#     yield i
#
# kii = generatorr()
# print(next(kii))
# print(next(kii))
# print(next(kii))
# print(next(kii))
#
# for j in kii:
#   print(j)


# colours = ["red", "green", "blue"]
# from itertools import permutations
# c = list(permutations(colours))
# print(c)

# a = [1,3,5,7,9  ]
# b = [1,2,4,6,7,8]
# diff1 = set(a) -set(b)
# diff2 = set(b) - set(a)
# maindiff = list(diff1)+list(diff2)
# print(maindiff)
#


# class Solution:
#     def twosum(self, numbers_list: list, target):
#         dict_to_store_values = {}
#         for index, value in enumerate(numbers_list):
#             difference = target - value
#             if difference in dict_to_store_values:
#                 return (dict_to_store_values[difference], index)
#             else:
#                 dict_to_store_values[value] = index
#
#
# b = Solution()
# a = b.twosum([2, 7, 11, 13], 9)
# print(a)


# cars = [
#   {'car': 'Ford', 'year': 2005},
#   {'car': 'Mitsubishi', 'year': 2000},
#   {'car': 'BMW', 'year': 2019},
#   {'car': 'VW', 'year': 2011}
# ]
#
# cars.sort(key=lambda x : x['year'])
# print(cars)


a = [1, 2, 3]
b = [4, 5, 6]

# print(a[::-1])
# print(b[::-1])

# c = zip(a,b)
# print(list(c))
# for i in c:
#   print(i)

# def my_generator():
#   for i in range(2, 100):
#     if i > 1:
#       for j in range(2, i):
#         if (i%j) == 0:
#           break
#       else:
#
#         yield i
#
# gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


# def greet(gr):
#     def ngreet(*args, **kwaargs):
#         print("Hello Pratik")
#         gr(*args, **kwaargs)
#         print("Its done in this way")
#
#     return ngreet
# @greet
# def add(a, b):
#     print(a + b)
#
# add(1,2)


# def div(a, b):
#   print(a/b)
#
#
#

# i = 2
# while(i< 21):
#   if i%2 == 0:
#     i += 2
# #     print(i)
#
# i = 1
# while(i<=20):
#
#     i += 2
#     print(i)

# i = 0
# while (i<300):
#   i = i + 10
#   print(i)


# i = 11
# while (i<=11):
#   i +=i
#   print(i)

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# l = []
# for rows in matrix:
#     for every_number_in_row in rows:
#         if every_number_in_row>1:
#             for num in range(2, every_number_in_row):
#                 if (every_number_in_row%num) == 0:
#                     break
#             else:
#                 l.append(every_number_in_row)
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         for k in l:
#             if matrix[i][j] == k:
#                 matrix[i][j] = True
# print(matrix)


