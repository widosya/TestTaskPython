# TestTaskPython
## Задание 1
На языке Python реализовать алгоритм (функцию) определения четности целого числа, который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути.\
Объяснить плюсы и минусы обеих реализаций.

Python example:
```
def isEven(value):return value%2==0
```
## Решение
```
def isEven(value): return value & 1 == 0 == value
```

Данная реализация использует более быструю операцию - побитовое "и". Некоторые компиляторы не производят оптимизацию и при делении по модулю может быть вызвана более дорогая инструкция деления.
## Задание 2

На языке Python (2.7) реализовать минимум по 2 класса реализовывающих циклический буфер FIFO.\
Объяснить плюсы и минусы каждой реализации.

## Решение
В файле RingQueueList.py представлена реализация цикличного буфера с помощью списка. Реализованы методы проверки на пустоту и полноту, проверки размера, добавления и удаления элемента в начале очереди, получения элемента по индексу и метод получения первого в очереди элемента. 
Принцип FIFO соблюден. При добавлении нового элемента в полностью заполненный буфер самый старый элемент будет удален.

Плюсы:
1. Доступ ко всем элементам происходит за О(1);
2. Более простая реализация.

Минусы:
1. Количество расходуемой памяти больше, так как создается список.

В файле RingQueueList.py представлена реализация с помощью двусвязного списка. Реализованы методы проверки на пустоту и полноту, проверки размера, добавления и удаления элемента в начале очереди, получения элемента по индексу и метод получения первого либо последнего в очереди элемента.
Принцип FIFO соблюден. При добавлении нового элемента в полностью заполненный буфер самый старый элемент будет удален.

Плюсы:
1. Доступ ко элементам в начале и конце очереди происходит за О(1);
2. При одинаковом размере списков занимает меньшее количество памяти.

Минусы:
1. Доступ к элементам внутри списка происходит за О(n).

## Задание 3
На языке Python реализовать функцию, которая быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел. Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным).\
Объяснить почему вы считаете, что функция соответствует заданным критериям.
Наиболее подходящими под описание задания являются Timsort и Introsort. Выбор был сделан в пользу Introsort, так как в случае, если в массиве будут уже упорядоченные числа, сложность Timsort станет О(n), когда как Introsort всегда сохраняет O(nlogn). Стабильность и сложность по памяти не учитывались.
