# This code is designed to replicate Collatz Conjecture
#Explaintion on Collatz Conjecture https://www.youtube.com/watch?v=094y1Z2wpJg
i = 1
number = int(input()
while i < 10:
             if number % 2 == 0:
                 number = number / 2
                 print (number)
             elif number % 2 ==1:
                 number = number*3
                 number = number +1
                 print (number)
            else:
             i=i+1
