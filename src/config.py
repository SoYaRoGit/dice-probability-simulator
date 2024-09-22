from pydantic import BaseModel, Field
from typing_extensions import Annotated


class InputModel(BaseModel):
    """Валидация входных данных на заданное число 10_000_000 >= x > 0"""

    counter: Annotated[
        int,
        Field(
            title="Счетчик",
            description="Количество подкидываний игральной кости",
            ge=1,
            le=10_000_000,
        ),
    ]
