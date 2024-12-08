#empty tuple
mytuple=()
print(mytuple)
#tuple with integer
mytuple=(1,2,3,4,5)
print(mytuple)
# tuple with mixed data type
mytuple=("harry",1,"larry",2.5)
print(mytuple)
#list in tuple , tuple in tuple
mytuple=("harry",[1,2,3],(4,5,6))
print(mytuple)
#deciding tuple
mytuple=('a','b','c','d','e')
print(mytuple[0])
print(mytuple[4])
#nesting tuple
mytuple=("harry",[1,2,3],(4,5,6))
print(mytuple)
print(mytuple[0][3])
print(mytuple[1][1])
#slice
mytuple=('a','b','c','d','e')
print(mytuple[0:2])
#etaration
for letter in (mytuple):
    print("hello " , letter)
    #finish