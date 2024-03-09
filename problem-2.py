def fibonacci(x):
    prev, new, temp, sum = 0, 1, 0, 0
    while True:
        prev = new
        new = temp
        temp = prev + new
        if temp < x:
            if temp % 2 == 0:
                sum = sum + temp
        else:
            break
    return sum

fibonacci(x)