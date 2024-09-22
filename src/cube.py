from collections import Counter
from random import randint


class Cube:
    """Игральная кость"""

    def __init__(self) -> None:
        self.data: list = []

    def roll_dice(self, quantity: int) -> dict[int, int]:
        """_summary_

        Args:
            quantity (int): количество подкидываний

        Returns:
            dict[int, int]: сортированный подсчет данных
        """
        # Очистить список перед броском
        self.data.clear()
        for _ in range(quantity):
            self.data.append(randint(1, 6))

        # Сортировка данных
        self.data.sort()
        return dict(Counter(self.data))


cube = Cube()
