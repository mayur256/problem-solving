socks = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n = len(socks)

def sockMerchant(n, socks):
    S = set(socks)
    pairs = 0
    socksCountList = []

    for el in S:
        socksCountList.append(socks.count(el))
    
    for count in socksCountList:
        pairs += count // 2    
    
    return pairs
    
print(sockMerchant(n, socks))
