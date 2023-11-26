from typing import List, Dict, Tuple


class TuringMachine:
    """Класс для эмуляции машины Тьюринга."""

    def __init__(self, alphabet: List[str]):
        """
        Инициализация машины Тьюринга.

        :param alphabet: Список символов алфавита, используемых машиной.
        """
        self.initial_state: str = 'q0'
        self.termination_state: str = '!'
        self.blank_symbol: str = '_'
        self.transition_rules: Dict[str, Dict[str, Tuple[str, str, str]]] = dict()
        self.current_state: str = self.initial_state
        self.tape: Dict[int, str] = dict()
        self.tape_position: int = 0
        self.alphabet: List[str] = alphabet if self.blank_symbol in alphabet else alphabet + [self.blank_symbol]

    def add_transition_rule(self, state: str, transitions: Dict[str, Tuple[str, str, str]]) -> None:
        """
        Добавление правил перехода для состояния.

        :param state: Строка, обозначающая состояние.
        :param transitions: Словарь переходов для данного состояния.
        """
        self.transition_rules[state] = transitions

    def load_tape(self, input_string: str) -> None:
        """
        Инициализация ленты значениями.

        :param input_string: Строка с начальными значениями для ленты.
        """
        for position, char in enumerate(input_string):
            self.tape[position] = char

    def perform_step(self) -> None:
        """
        Выполнение одного шага машины Тьюринга.

        :raises ValueError: Если символ или состояние не определены.
        """
        symbol = self.tape.get(self.tape_position, self.blank_symbol)
        if symbol not in self.alphabet:
            raise ValueError("Symbol not in alphabet")
        if self.current_state not in self.transition_rules:
            raise ValueError("State not defined")

        transition = self.transition_rules[self.current_state].get(symbol)
        if transition is None:
            raise ValueError("No transition defined")

        new_symbol, move_direction, new_state = transition
        self.tape[self.tape_position] = new_symbol

        if move_direction == 'L':
            self.tape_position -= 1
        elif move_direction == 'R':
            self.tape_position += 1

        self.current_state = new_state

    def execute(self, input_string: str) -> str:
        """
        Выполнение машины Тьюринга на входной строке.

        :param input_string: Строка для обработки на ленте машины.
        :return: Строка с результатами обработки.
        """
        self.load_tape(input_string)
        while self.current_state != self.termination_state:
            self.perform_step()
        return ''.join(self.tape.get(position, self.blank_symbol)
                       for position in range(min(self.tape), max(self.tape) + 1))

    def increment(self) -> None:
        """
        Добавляет правила переходов для увеличения числа на ленте машины.
        """
        self.add_transition_rule('q0', {'0': ('0', 'R', 'q0'),
                                                  '1': ('1', 'R', 'q0'),
                                                  '_': ('_', 'L', 'q1')})
        self.add_transition_rule('q1', {'0': ('1', 'N', 'q2'),
                                                  '1': ('0', 'L', 'q1'),
                                                  '_': ('1', 'N', '!')})
        self.add_transition_rule('q2', {'0': ('0', 'L', 'q2'),
                                                  '1': ('1', 'L', 'q2'),
                                                  '_': ('_', 'R', '!')})
    def invert(self) -> None:
        """
        Добавляет правила переходов для инверсии числа на ленте машины.
        """
        self.add_transition_rule('q0', {'0': ('1', 'R', 'q0'),
                                        '1': ('0', 'R', 'q0'),
                                        '_': ('_', 'N', '!')})


# Пример использования:
if __name__ == "__main__":
    alphabet = ['0', '1', '_']
    turing_machine = TuringMachine(alphabet)

    # Добавление состояний и переходов
    turing_machine.increment()

    # Запуск машины на входной строке
    output = turing_machine.execute('1101010110')
    print(output)  # Вывод результата выполнения
