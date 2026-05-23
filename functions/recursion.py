def function1(n):
    if n == 1:
        return 1
    else:
        return n * function1(n - 1)

result=function1(4)
print(result)