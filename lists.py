#lists are mutable :D

list1 = ["ami", "tumi", "shey", 1, 420.2]

for x in list1:
    print(x)

list2 = [list1, list1,list1]
print(list2)
for x in list2:
    for y in x:
        print(y,end=" ")
print()
for x in range (0,len(list2)):
    for y in range(0,len(list2[x])):
        print(list2[x][y],end=",")
    print()
