import numpy as np

def score_game(random_predict) -> int:
    """Генератор случайных чисел. Создает список случайных чисел для
       проверки функции на поиск числа
    Args:
        random_predict (_type_): _description_

    Returns:
        int: _description_
    """
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls)) # находим среднее количество попыток
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

def number_find (index_start:int,index_end:int,number:int,count:any):
    """Рекурсивная функция поиска числа. Ищет методом деления пополам. 
       Получает крайние значения,искомое число и значение счетчика. Находит 
       среднее между ними. После этого если среднее - не найденное число 
       обращается к самой себе, увеличивая значение счетчика на 1

    Args:
        index_start (int): _description_
        index_end (int): _description_
        number (int): _description_
        count (any): _description_

    Returns:
        _type_: _description_
    """
    count +=1
    ugadayka=index_start+(index_end-index_start)//2

    if ugadayka==index_start:
        ugadayka +=1

    if ugadayka>number:
        count = number_find (index_start, ugadayka, number, count)

    elif ugadayka<number:
        count = number_find (ugadayka, index_end, number, count)

    return count
 
def random_predict(number:int=1) -> int:
    """ Функция поиска случайного числа. Обращается к рекурсивной функции
        В результате выдает количество попыток поиска числа

    Args:
        number (int, optional): _description_. Defaults to 1.

    Returns:
        int: _description_
    """

    count = 0
    count = number_find(1, 101, number, count)
    return(count)
