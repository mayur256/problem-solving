def generateFiboSequence(n):
    """Function that generates a fibonnaci sequence upto number n"""
    a,b=0,1
    while a<=n:
        print(a, end=' ')
        a,b=b,a+b
    print()
generateFiboSequence(5)
