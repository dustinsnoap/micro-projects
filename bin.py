def test(n):
    print(bin(n)[2:][::-1])
    print('n', n)
    n = bin(n)[2:]
    print('n2', n)
    n = n[::-1]
    print('n3', n)
    n = int(n,2)
    print('n4', n)



test(237)