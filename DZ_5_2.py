# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”. В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии
# Ввод:
# name_list = ['Vlad', 'Den', 'Alex']
# salary_list = [1000, 2000, 3000]
# extra_list = ['10.25%', '15%', '20%']
# Вывод:
{'Vlad': 102.5, 'Den': 300.0, 'Alex': 600.0}

name_list = ['Vlad', 'Den', 'Alex']
salary_list = [1000, 2000, 3000]
extra_list = ['10.25%', '15%', '20%']

i = 0
rez_dict = {}
while i < len(name_list ):
    n = name_list[i]
    s = salary_list[i]
    e = extra_list[i]
    i+=1
    premium = float(e.split('%')[0])*s/100
    rez_dict[n] = premium
print (rez_dict)


# Создайте функцию генератор чисел Фибоначчи
# def fib(n):
#     res_out = [0, 1]
#     for i in range(n):
#         sum = res_out[i] + res_out[i+1]
#         res_out.append(sum)
#     return res_out
#
# print(fib(100))