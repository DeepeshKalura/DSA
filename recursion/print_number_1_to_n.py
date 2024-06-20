def reverse_recursion_print(n:int) -> None:
    if(n == 0):
        return 

    print(n,end=" ")
    reverse_recursion_print(n-1)



def recursion_print(n:int) -> None:
    if( n == 0):
        return  
    recursion_print(n-1)
    print(n, end=" ")


n = 10
recursion_print(10)
print()
reverse_recursion_print(10)
print()




