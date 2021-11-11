# This code is designed to replicate Collatz Conjecture
#Explaintion on Collatz Conjecture https://www.youtube.com/watch?v=094y1Z2wpJg
i=1
n=int(input('Please enter a number to prove Collatz Conjecture '))
while i==1:
    if n % 2 == 0:
        n=n/2
        print (n)
    else:
        n=n*3
        n=n+1
        print (n)
