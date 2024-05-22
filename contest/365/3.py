from functools import reduce
n = 3
x = 4

array = [x]

a = bin(x)

print(a)
print(a[2:]) 

b = ""
for i in range(len(a[2:])):
    b+="1"

print(b)
max_element = int(b, 2)

print(max_element)


i = 1
while(n>1):
    array.append(x+i)
    i+=1
    n-=1

# y = reduce(lambda a,b: a & b, array )
y = array[0]
for i in range(1, len(array)):
    y = y & array[i]
    print(y)

# print(y)
if(x==y):
    print("pass")
else:
    print("Fail")

print(array)

print("End of the program")