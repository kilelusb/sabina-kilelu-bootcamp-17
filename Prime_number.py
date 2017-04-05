
def prime_numbers(n):
    prime =[]
    if type(n) == int:
        if n>1:
            not_prime = set(j for i in range(2,n+1) for j in range(i*2,n+1, i))
            for i in range(2,n+1):
                if i not in not_prime:
                    prime.append(i)
                    return prime
    elif type(n)==str:
        return 'Not a prime number'
    elif type(n)==list:
        return 'Not a prime number'
    else:
        pass
    
    
