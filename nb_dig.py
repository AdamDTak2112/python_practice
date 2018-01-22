def nb_dig(n, d):
    # your code
    numList = []
    count = 0
    dword = str(d)
    for temp in range(1, n):
        numList.append(str(temp))
    for item in numList:
        for x in item:
            if x == dword:
                count += 1
