def fibonacci(n):
    x=0
    y=1
    while y<n:
        z=x+y
        x=y
        y=z
    if y==n:
        return True
    else:
        return False
num=int(input())
if fibonacci(num):
    print("True")
else:
    print("False")