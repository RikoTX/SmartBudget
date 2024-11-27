# src/services/transaction_service.py

from DatabaseModule.data_module import read_balance, write_balance, read_transactions, write_transaction

def add_transaction(amount, description, transaction_type):
    balance = read_balance()
    
    # Обновляем баланс в зависимости от типа транзакции
    if transaction_type == 'Доход':
        balance += amount
    elif transaction_type == 'Расход':
        balance -= amount

    # Записываем обновленный баланс в файл
    write_balance(balance)

    # Добавляем транзакцию в историю
    transaction = f"{transaction_type}: {amount} ({description})"
    write_transaction(transaction)

def get_balance():
    return read_balance()

def get_transactions():
    return read_transactions()
