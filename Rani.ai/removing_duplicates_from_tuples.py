test_tup = (1, 3, 5, 2, 3, 5, 1, 1, 3)
print("first tuple is : " + str(test_tup))
res = tuple(set(test_tup))

print("tuple after removing duplicates : " + str(res))