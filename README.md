# Эмулятор машины Тьюринга

Этот проект является реализацией эмулятора машины Тьюринга на Python. Машина Тьюринга — это фундаментальная модель вычислений, которая манипулирует символами на ленте в соответствии с таблицей правил.

## Особенности

- Инициализация машины Тьюринга с произвольным алфавитом.
- Загрузка входной ленты строкой символов.
- Определение переходов состояний и правил для машины Тьюринга.
- Выполнение машины для обработки входной ленты.
- Включает методы для увеличения и инвертирования двоичных чисел на ленте.

## Требования

- Python версии 3.6 или выше

## Использование

Вот простой пример использования класса машины Тьюринга:

```python
from turing_machine import TuringMachine

# Определяем алфавит и создаем экземпляр машины Тьюринга
alphabet = ['0', '1', '_']
turing_machine = TuringMachine(alphabet)

# Добавляем состояния и переходы
turing_machine.invert()

# Запускаем машину с входной строкой
output = turing_machine.execute('110101011')
print(output)  # Выводит результат выполнения
```

## Настройка машины

Для настройки поведения машины вы можете определить новые правила перехода с помощью метода `add_transition_rule`.

