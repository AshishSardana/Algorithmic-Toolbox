#python2
# Author: Ashish Sardana
import sys

input = sys.stdin.read();
n, m = map(int, input.split())

a = [0,1,1]

if n==0:
    print 0
elif n==1:
    print 1
else:
    for i in range (2,n+1):
            b = a[i-1]+a[i]
            b=b%m
            a.append(b)
    print a[n]



