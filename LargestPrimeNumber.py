
primes = []

def GetSmallestPrimeFactor(num):
    for i in range(2, num):
        if (num%i) == 0:
            return i

def GetLargestPrimeFactor(num):
    smallestFactor = GetSmallestPrimeFactor(num)
    limit = int(num/smallestFactor)
    print(limit)
    
    for i in range(2, limit+1):
        if (num%i) == 0:
            tot = 0
            for a in range(1, i+1):
                if(i%a) == 0:
                    tot += 1
            
            if tot == 2:
                primes.append(i)


    return 0;

GetLargestPrimeFactor(600851475143)
print("The primes are: ", primes)