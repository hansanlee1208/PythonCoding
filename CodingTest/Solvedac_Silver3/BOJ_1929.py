def is_prime(n):
    if n <= 1:
        return  False
    for i in range(2, n):
        if n % i  == 0:
            return  False
    return True
print(is_prime(11))

def sieve_of_eratosthenes(min_num, max_num):
    is_prime = [True] * (max_num + 1)
    p = 2
    while p * p <= max_num:
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = [p for p in range(min_num, max_num + 1) if is_prime[p]]
    return prime_numbers

M, N = map(int, input().split())
l_list = []
l_list = sieve_of_eratosthenes(M, N)
for i in l_list:
    print(i)