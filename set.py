myset={1,2,2,3,4,5,6,6,7,78,3}
print("set",myset)
myset.add(9)
print("updated set",myset)
set1=myset
set2={2,4,4,10}
print("set1",set1)
print(" set2",set2)
print("difference",set1.difference(set2))
print("symetric difference",set1.symmetric_difference(set2))
