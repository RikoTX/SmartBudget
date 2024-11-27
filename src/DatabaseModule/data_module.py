# C:\Users\User\Desktop\SmartBudget\src\DatabaseModule\data_module.py

# Путь к файлам
BALANCE_FILE_PATH = "C:\\Users\\User\\Desktop\\SmartBudget\\src\\DatabaseModule\\balance.txt"
TRANSACTIONS_FILE_PATH = "C:\\Users\\User\\Desktop\\SmartBudget\\src\\DatabaseModule\\transactions.txt"

# Функция для чтения баланса
def read_balance():
    try:
        with open(BALANCE_FILE_PATH, "r") as file:
            balance = file.read().strip()  # Читаем баланс из файла
            return float(balance) if balance else 0.0  # Преобразуем в float и возвращаем
    except FileNotFoundError:
        return 0.0  # Если файл не найден, возвращаем 0.0

# Функция для записи баланса
def write_balance(balance):
    try:
        with open(BALANCE_FILE_PATH, "w") as file:
            file.write(str(balance))  # Записываем баланс в файл
    except Exception as e:
        print(f"Ошибка при записи баланса: {e}")

# Функция для загрузки баланса (переименование read_balance в load_balance)
def load_balance():
    return read_balance()  # Переименованный вызов read_balance

# Функция для сохранения баланса (переименование write_balance в save_balance)
def save_balance(balance):
    write_balance(balance)  # Переименованный вызов write_balance

# Функция для загрузки транзакций
def load_transactions():
    try:
        with open(TRANSACTIONS_FILE_PATH, "r") as file:
            transactions = file.readlines()  # Читаем все строки из файла
            return [transaction.strip() for transaction in transactions]  # Убираем лишние пробелы
    except FileNotFoundError:
        return []  # Если файл не найден, возвращаем пустой список

# Функция для сохранения транзакций
def save_transactions(transactions):
    try:
        with open(TRANSACTIONS_FILE_PATH, "w") as file:
            for transaction in transactions:
                file.write(transaction + "\n")  # Записываем каждую транзакцию в новую строку
    except Exception as e:
        print(f"Ошибка при записи транзакций: {e}")
