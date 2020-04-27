"""
Apple and Orange: https://www.hackerrank.com/challenges/apple-and-orange/problem

"""

def countApplesAndOranges(s, t, a, b, m, n, apples, oranges):
    count_app=0
    count_ora=0
    for i in range(m):
        f=a+apples[i]
        if( f>=s and f<=t):
            count_app+=1
    print(count_app)
    for i in range(n):
        f=b+oranges[i]
        if(f>=s and f<=t):
            count_ora+=1
    print(count_ora)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, m, n, apples, oranges)
 
