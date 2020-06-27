def num(sum):
    previous=0
    for i in range(0,10+1):
       s=i+previous
       print('current number is',i,'previous nunber is',previous,'sum',s)
       previous=i       
print("printing current number & previous number a in range of (10)")
num(10)