from config import InputModel
from cube import cube


def main() -> None:
    try:
        user_input = int(input("Введите количество подкидываний: "))
        user_input_model = InputModel(quantity=user_input)
        quantity: int = user_input_model.quantity
        data: dict[int, int] = cube.roll_dice(quantity)

        for key, value in data.items():
            print(f"Количество {key} = {value}")

    except ValueError as e:
        print(f"[ERROR]: {e}")


if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("[INFO]: Программа принудительно остановлена!")
