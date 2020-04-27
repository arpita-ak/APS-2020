"""
LONGCOOK

"""

T=int(input())


def WhichDay(day,month,year):
	t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
	year -= month < 3
	return (year + int(year/4) - int(year/100) + int(year/400) + t[month-1] + day) % 7

def IsLeap(y):
    if y%4==0:
        if y%100==0:
            if y%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
  


for i in range(T):
    X=list(map(int,input().strip().split()))
    Y=list(map(int,input().strip().split()))
    
    m1=X[0]
    y1=X[1]
    
    m2=Y[0]
    y2=Y[1]
    
    if m1>2:
        y1+=1
    if m2==1:
        y2-=1
      
    w=WhichDay(1,2,y1)
    count=0
    
    for i in range(y1,y2+1):
        if IsLeap(i)==True:
            if w%7==6:
                count+=1
            w+=2
        else:
            if w%7==6 or w%7==0:
                count+=1
            w+=1
        
    print(count)
   