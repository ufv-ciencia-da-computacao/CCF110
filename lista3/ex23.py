fib = 0; lastFib = 1; secondLastFib = 1
for i in range(1,21):
    if i == 1 or i == 2:
        print(1)
    else:
        fib = lastFib + secondLastFib
        secondLastFib = lastFib 
        lastFib = fib
        print(fib)