"""Модуль для игры в конфетки с чатботом."""


class Candy_Game:
    """Высшая функция."""

    def __init__(self, candy_num=123, user_name='unknown'):
        """Инициализация."""
        import random
        candy_num = random.randint(50, 200)
        self.candy_num = candy_num
        self.user_name = user_name

    def StartMessage(self):
        """Doc."""
        return ["continue", f"Начнем с {self.candy_num} \U0001F36C"]

    def CandyGameWin(self, num: int, ) -> int:
        """Возвращает лучшее решение или 28."""
        res = 28
        if num % 29:
            res = num % 29
        return res

    def UserTurn(self, num_str: str) -> list:
        """Doc."""
        try:
            num = int(num_str)
        except TypeError:
            return ["continue", "введите число от 0 до 28"]

        if num > 28 or num > self.candy_num:
            return [
                "continue", "возьмите, пожалуйста, меньше \U0001F36C (до 28)"]
        else:
            self.candy_num -= num
        if self.candy_num == 0:
            return ["end", "Вы выиграли! \U0001F92F  Поздравляю!"]
        bot_take = self.CandyGameWin(self.candy_num)
        self.candy_num -= bot_take
        if self.candy_num == 0:
            return [
                "end", f"Я забрал {bot_take} \U0001F36C и выиграл!\U0001F973"]
        else:
            return ["continue", f"Я забрал {bot_take} \U0001F36C, осталось "
                    f"{self.candy_num}\U0001F36C"]


if '__name__' == '__main__':
    new_game = Candy_Game
