def fizz_buzz_custom(numbers, fizz=3, buzz=5, fizz_buzz=15, 
                     fizz_word='Fizz', buzz_word='Buzz', fizz_buzz_word='Fizz_Buzz'):
    """
    Функция FizzBuzz с кастомизацией делителей и слов
    
    numbers: последовательность чисел для обработки
    fizz: делитель для первого слова
    buzz: делитель для второго слова
    fizz_buzz: делитель для обоих слов
    fizz_word: Слово для чисел, кратных fizz
    buzz_word: Слово для чисел, кратных buzz
    fizz_buzz_word: Слово для чисел, кратных fizz_buzz
    return: список обработанных значений
    """
    result = []
    for i in numbers:
        if fizz_buzz and i % fizz_buzz == 0:
            result.append(fizz_buzz_word)
        elif fizz and i % fizz == 0 and i % buzz != 0:
            result.append(fizz_word)
        elif buzz and i % buzz == 0:
            result.append(buzz_word)
        else:
            result.append(i)
    return result

# переменные для проверки функции
tuple = tuple(range(1, 16))
set = set(range(50, 65))

# применение функции
# стандартный FizzBuzz
print(fizz_buzz_custom([1, 2, 3, 4, 5, 15]))
print(fizz_buzz_custom(tuple))

# кастомные делители и слова
print(fizz_buzz_custom(set, fizz=7, buzz=9, fizz_buzz=63, 
                       fizz_word='Seven', buzz_word='Nine', fizz_buzz_word='Combo'))

print(fizz_buzz_custom(range(1, 25), fizz=2, buzz=4, fizz_buzz=8, 
                       fizz_word='Even', buzz_word='Quad', fizz_buzz_word='Octo'))

# На примере с делителями, которые являются квадратами от первого делителя (fizz) хорошо видно, 
# как работает функция, например:
# если число делится на 8, на 4 и на 2, то замена осуществляется по максимальному делителю fizz_buzz (8)
# если число делится на 4 и на 2, то замена осуществляется по среднему делителю buzz (4)
# если число делится только на 2, то замена осуществляется по минимальному делителю fizz (2)
# У функции есть ограничение - параметры fizz, buzz, fizz_buzz нужно указывать в порядке возростания


