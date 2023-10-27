def find_diff(n):
    product=1
    sum=0
    for digit in str(n):
        product*=int(digit)
        sum+=int(digit)
    return product-sum
n=int(input())
print(find_diff(n))