
def prime_numbers(n):
    prime = True
    if type(n) == int:
        if n>=1:
            for i in range(0,n+1):
                if i%2==1:
                    prime.append(i)
                    return prime
        elif (num%i==0) or n<=0:
            prime = False
    if prime:
        print (num)
    
    
