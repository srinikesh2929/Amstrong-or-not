
num = int(input("Enter the number"))
n = num
sum = 0
while n > 0:
    a = n % 10
    sum = sum+a*a*a
    n = int(n/10)

print(sum)
if sum == num:
    print("armstrong")
else:
    print("Not armstrong")
