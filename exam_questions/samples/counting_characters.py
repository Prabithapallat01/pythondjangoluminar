def FirstFactorial(n):
    f=1
    for i in range(1,n+1):
       f=f*i
  # code goes here
    return f


num=int(input())
result=FirstFactorial(num)
# keep this function call here
print(result)
