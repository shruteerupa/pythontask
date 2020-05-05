def fibonaci(n):
    a=0
    b=1
    count=0
    if n<0:
        return  'not possibe'
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        while count<n:
            print(a)
            temp=a+b
            a=b
            b=temp
            count+=1

num=int(input('énter the number'))
result=fibonaci(num)
print(result)


import math

def CheckPerfect(x):
  i = int(math.sqrt(x))
  return (x == i*i)

def CheckFibo(n):
  if(CheckPerfect(5*n*n + 4) or CheckPerfect(5*n*n - 4)):
    print("Fibonacci")
  else:
    print("Not Fibonacci")


result=CheckFibo(num)
print(result)
