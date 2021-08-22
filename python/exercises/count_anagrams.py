def makeAnagrams(a,b):
    count = 0

    for i in range(ord('a'),ord('z')+1):
        chars_in_a = a.count(chr(i))
        chars_in_b = b.count(chr(i))
        count += abs(chars_in_a - chars_in_b)
    return(count)


if __name__ == '__main__':
    s1="asdkj;asdjkl"
    s2="-0;askljd;laskd"

    print(makeAnagrams(s1,s2))


    s1='aabaabaa'
    s2='aaba'
    print(makeAnagrams(s1,s2))
