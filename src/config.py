from pydantic import BaseModel, PositiveInt


class InputModel(BaseModel):
    """Валидация входных данных на заданное число > 0"""

    counter: PositiveInt
