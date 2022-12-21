"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""
import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    predict_number = np.random.randint(1, 101) # загадываем рандомное число, используя генератор рандомных чисел
    count = 0 # Переменная счетчик
    min_num = 1 # Минимальное значение рассматриваемого интервала
    max_num = 100 # Максимальное значение рассматриваемого интервала
    while True:
        count += 1
        if predict_number > number:
            max_num= predict_number - 1
            predict_number = (max_num + min_num) // 2
        elif predict_number < number:
            min_num = predict_number + 1
            predict_number = (max_num + min_num) // 2
        else:
            break
    return(count)


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)
