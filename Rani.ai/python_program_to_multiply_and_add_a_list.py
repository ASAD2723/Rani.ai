def multiplyaddList(myList) :
    result = 1
    for lst in myList:
         result = result * lst
    return result

list1 = [10, 21, 56]
list2 = [43, 22, 43]
print(multiplyaddList(list1))
print(multiplyaddList(list2))
print(multiplyaddList(list1) + multiplyaddList(list2))