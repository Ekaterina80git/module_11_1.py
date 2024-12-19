
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


print('библиотека Python: requests')


class Requests:
    url = 'https://www.tbank.ru'  # Указываем URL, на который будем отправлять GET-запрос
    response = requests.get(url)  # Отправляем GET-запрос по указанному URL
    if response.status_code == 200:  # Проверяем статус-код ответа
        data = response.url  # Если статус-код 200 (OK), получаем данные из ответа
        print(f'Статус ответа: OK [код 200]')
    else:
        print('Ошибка при выполнении запроса')  # При ошибке будет данное сообщение


print('библиотека Python: pandas')


class Pandas:
     # Загрузка данных из текстового файла
     data = pd.read_fwf(r'C:\Users\Huawei\PycharmProjects\pythonProject1\example4.txt')

     # Отображение первых 6 строк данных
     print(data.head(6))


print('библиотека Python: nympy')


class Numpy:
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])  # Создаем массив
    sum = np.sum(arr)   # Суммируем его элементы
    flip = np.flip(arr) # Элементы массива в обратном порядке

    print(arr)
    print(sum)
    print(flip)

print('библиотека Python: matplotlib')


class Matplotlib:
    # Задаем данные по осям
    year = [1950, 1975, 2000, 2018]
    population = [2.12, 3.681, 5.312, 6.981]

    # Построение линейного графика
    plt.plot(year, population)
    plt.show()
    plt.xlabel('Год')
    plt.ylabel('Популяция')
    plt.title('Линейный графика')








