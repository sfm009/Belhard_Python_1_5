"""
СОРТИРОВКА ВЫБОРКОЙ

Этот алгоритм сегментирует список на две части:
отсортированную и неотсортированную.
Наименьший элемент удаляется из второго списка и добавляется в первый.
На практике не нужно создавать новый список для отсортированных элементов.
В качестве него используется крайняя левая часть списка.
Находится наименьший элемент и меняется с первым местами.

Теперь, когда нам известно, что первый элемент списка отсортирован,
находим наименьший элемент из оставшихся и меняем местами со вторым.
Повторяем это до тех пор, пока не останется последний элемент в списке.

По мере увеличения значения i нужно проверять меньше элементов.

ВРЕМЯ СОРТИРОВКИ: в среднем O(n²)
"""


def selection_sort(array: list) -> list:
    for i in range(len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array) - 1):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


if __name__ == '__main__':
    assert selection_sort([2, 1, 5, 4, 7]) == [1, 2, 4, 5, 7]
    assert selection_sort([2, -5, -3, 3, 1, 2]) == [-5, -3, 1, 2, 2, 3]
    print('Решено!')
