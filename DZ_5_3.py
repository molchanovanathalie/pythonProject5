# Создайте функцию генератор чисел Фибоначчи

def fib(n):
    res_out = [0, 1]
    for i in range(n):
        sum = res_out[i] + res_out[i+1]
        res_out.append(sum)
    return res_out

print(fib(10))