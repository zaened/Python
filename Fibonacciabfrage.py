# author : Zäned Pasagad
# date : 07.05.2021

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end = ' ')
        a, b = b, a + b

fib(int(input('Geben sie eine Zahl ein: ')))
    

