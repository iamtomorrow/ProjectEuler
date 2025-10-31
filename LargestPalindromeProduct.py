
palindromes = []

def GetLargestPalindromeProduct( ):
    a = 999
    while a > 0:
        i = 999
        while i > 900:
            product = f"{i*a}"
            if product == product[::-1] and len(f"{i}") == 3 and len(f"{a}") == 3:
                print(a, i)
                return product
            i-=1
        a-=1

print( GetLargestPalindromeProduct( ) )