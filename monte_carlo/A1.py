from sympy import isprime
import math

def LCG(x0,a,c,m):
    x = (a*x0 + c) % m
    return x


#========== Question 1
result = [[1],[4],[7]]

for x in result:
    for j in range(0,3):
        term = LCG(x[j],5,7,13)
        x.append(term)

#print(result)


#========Q2========

result2 = [0]

for i in range(0,20):
    term = LCG(result2[i],3,1,13)
    result2.append(term)

#print(result2)



# hull dobell check for period 
m = 134456
a = 8121
def rel_prime(a,b):
    return math.gcd(a,b)==1

print(rel_prime(8121,134456))

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

#print(set(prime_factors(134456)))
#print(set(prime_factors(8121 -1)))

#print((a-1) % 4 == 0 and m % 4 == 0)

print(math.ceil(math.log(0.54) / math.log(0.9)))