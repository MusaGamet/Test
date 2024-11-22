def read_from_file(file_name):
    """
    Функция №1: Читает строки из файла и возвращает их в виде списка.
    """
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()
        return [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_name} не найден.")
        return []

def display_lines(lines):
    """
    Функция №2: Выводит строки на экран.
    Пока ничего не делает.
    """
    pass

def write_to_file(file_name, lines):
    """
    Функция №3: Записывает строки в файл.
    Пока ничего не делает.
    """
    pass

def main():
    # Пока просто вызов пустых функций
    file_to_read = "input.txt"
    file_to_write = "output.txt"

    # Вызов функций
    lines = read_from_file(file_to_read)
    display_lines(lines)
    write_to_file(file_to_write, lines)

if __name__ == "__main__":
    main()

