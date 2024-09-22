from config import InputModel


def main() -> None:
    try:
        user_input = int(input("Введите количество подкидываний: "))
        user_input_model = InputModel(counter=user_input)
        counter: int = user_input_model.counter
        print(counter)
    except ValueError as e:
        print(f"[ERROR]: {e}")


if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("[INFO]: Программа принудительно остановлена!")
