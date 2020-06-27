# Range number sum into privious number
- **Print the Range values.**
- **Range Values Add into the Privious Values.**
# Sample Code For Range number sum into privious number
```
previous=0
for i in range(0,10+1):
    s=i+previous
    print('current number is',i,'previous nunber is',previous,'sum',s)
    previous=i    
```
# Example Ouput
```
printing current number & previous number range of (10)
current number is 0 previous nunber is 0 sum 0
current number is 1 previous nunber is 0 sum 1
current number is 2 previous nunber is 1 sum 3
current number is 3 previous nunber is 2 sum 5
current number is 4 previous nunber is 3 sum 7
current number is 5 previous nunber is 4 sum 9
current number is 6 previous nunber is 5 sum 11
current number is 7 previous nunber is 6 sum 13
current number is 8 previous nunber is 7 sum 15
current number is 9 previous nunber is 8 sum 17
current number is 10 previous nunber is 9 sum 19
```
