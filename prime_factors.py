def prime_fac(n):
    for i in range(1,n+1):
        if n%i == 0:
            for j in range(2, i):
                if i%j == 0:
                    break
            else:
                yield i


number = int(input('Enter a number'))
for x in prime_fac(number):
    print(x)
