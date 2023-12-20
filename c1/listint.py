list1=[2,6,1,9]
list2=[3,5,8]
print(list1)
print(list2)
if(len(list1)==len(list2)):
    print("lists are of same length.")
else:
    print("lists are not the same length.")
print("sum of list 1 =",sum(list1))
print("sum of list 2 =",sum(list2))
if(sum(list1)==sum(list2)):
    print("sum of 2 lists are same.")
else:
    print("sum of 2 lists are not same.")
check=any(item in list1 for item in list2)
print("any value occur in both",check)
