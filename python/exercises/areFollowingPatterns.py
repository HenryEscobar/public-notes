def areFollowingPatterns(strings, patterns):

    hash_a = {}
    hash_b = {}
     
    for i, (x,y) in enumerate(zip(strings, patterns)):
        print("i: {i}\tx:{x}\ty:{y}".format(i=i,x=x,y=y))
        p1 = hash_a[x] = hash_a.get(x,i)
        p2 = hash_b[y] = hash_b.get(y,i)
        if p1 != p2:
            return False
    return True
