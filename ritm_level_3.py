def fizz_buzz_custom(numbers, *dividers_and_words):
    """
    Функция FizzBuzz с кастомизацией делителей и слов 
    
    numbers: последовательность чисел для обработки
    dividers_and_words: пары (делитель, слово) в виде произвольного количества аргументов
    return: cписок обработанных значений
    """
    result = []
    for i in numbers:
        string = ""
        for divider, word in dividers_and_words:
            if i % divider == 0:
                string += word
        result.append(string if string else i)
    return result


# переменная для проверки функции
numbers = range(1, 21)

# применение функции
# с делителями 3, 5, 15
print(fizz_buzz_custom(numbers, (3, 'Fizz'), (5, 'Buzz'), (15, 'Fifteen')))

# с дополнительным делителем 7
print(fizz_buzz_custom(numbers, (3, 'Fizz'), (5, 'Buzz'), (15, 'Fifteen'), (7, 'Seven')))

# с другими кастомными словами и делителями
print(fizz_buzz_custom(numbers, (4, 'Four'), (6, 'Six')))

# Для корректной работы, в качестве аргументов функции, нужно передовать последовательность чисел numbers (список, range, кортеж и т. д.)
# и пары в виде кортежа (делитель, слово) *dividers_and_words, количество таких пар не ограничено.
 
# Функция проходит по каждому элементу i в numbers, 
# формирует строку в которой аккумулируется слова соответствующие делителям,
# проверяет число i на кратность каждому делителю, переданному в функцию,
# если число кратно делителю, к строке добавляется соответствующее слово,
# если число не кратно ни одному из делителей, в result добавляется само число,
# возвращает список, где числа заменены словами, если они кратны хотя бы одному из делителей,
# и многосоставными словами, если кратны сразу нескольким делителям.
