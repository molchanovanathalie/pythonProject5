
# Урок 5. Итераторы и генераторы
# Напишите функцию, которая принимает на вход
# строку - абсолютный путь до файла. Функция возвращает
# кортеж из трёх элементов: путь, имя файла, расширение файла.
# Ввод: c:/Users/Vladislav/Desktop/deep_to_python/test.txt
# Вывод: ( 'c:/Users/Vladislav/Desktop/deep_to_python/', 'test', 'txt')


def cortege(text):
    rez = []
    file_type = (text.split('.')[-1])
    slice = (text.split('.')[0])
    file_name = (slice.split('/')[-1])
    address = (slice.split(file_name)[0])
    rez.append(address, )
    rez.append(file_name)
    rez.append(file_type)
    return tuple(rez)

text = 'c:/Users/Vladislav/Desktop/deep_to_python/test.txt'
print(cortege(text))





