import math 
import random

def isPerfectSq(x): 
q = int(math.sqrt(x)) 
return q*q == x 

def isFibonacci(List=[]):
for n in List:
if isPerfectSq(5*n*n + 4) or isPerfectSq(5*n*n - 4):
FiboList.append(n)


List=[]
FiboList=[]


for i in range(100):
r=random.randint(0,100)
if r not in List: List.append(r)


print('Given List of Integers', List)
isFibonacci(List)
print('\nNumbers in the given List That belong to fibonacci Series : ', FiboList)