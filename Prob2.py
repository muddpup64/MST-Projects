print("Enter a whole number to be printed in Standard Factored Form: ")
num = int(input())
a = []
while num % 2 == 0:
    a.append(2)
    num /= 2
f = 3
while f * f <= num:
    if num % f == 0:
        a.append(f)
        num /= f
    else:
        f += 2
if num != 1: a.append(int(num))
# Only odd number is possible
print (a)