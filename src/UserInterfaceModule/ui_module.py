import tkinter as tk
from tkinter import messagebox
from DatabaseModule.data_module import load_balance, save_balance, load_transactions, save_transactions
from GoalModule.goal_service import load_goal, save_goal, update_goal_progress

# Создаем окно приложения
root = tk.Tk()
root.title("Учёт личных финансов")
root.geometry("500x700")  # Увеличим размер окна для добавления целей

# Метки и поля для ввода данных
balance_label = tk.Label(root, text="Баланс: 0.0")
balance_label.pack()

amount_label = tk.Label(root, text="Сумма:")
amount_label.pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

description_label = tk.Label(root, text="Описание:")
description_label.pack()
description_entry = tk.Entry(root)
description_entry.pack()

transaction_type = tk.StringVar()
income_radio = tk.Radiobutton(root, text="Доход", variable=transaction_type, value="Доход")
income_radio.pack()
expense_radio = tk.Radiobutton(root, text="Расход", variable=transaction_type, value="Расход")
expense_radio.pack()

add_transaction_button = tk.Button(root, text="Добавить транзакцию")
add_transaction_button.pack()

# Новый интерфейс для цели
goal_label = tk.Label(root, text="Цель накопления:")
goal_label.pack()

goal_amount_label = tk.Label(root, text="Сумма цели:")
goal_amount_label.pack()
goal_amount_entry = tk.Entry(root)
goal_amount_entry.pack()

goal_description_label = tk.Label(root, text="Описание цели:")
goal_description_label.pack()
goal_description_entry = tk.Entry(root)
goal_description_entry.pack()

set_goal_button = tk.Button(root, text="Установить цель")
set_goal_button.pack()

goal_progress_label = tk.Label(root, text="Прогресс цели: 0.0")
goal_progress_label.pack()

history_label = tk.Label(root, text="История транзакций:")
history_label.pack()

history_text = tk.Text(root, height=10, width=50)
history_text.pack()

# Обновление баланса, цели и истории
def update_ui():
    balance = load_balance()  # Загрузка текущего баланса
    balance_label.config(text=f"Баланс: {balance:.2f}")  # Обновление метки с балансом

    transactions = load_transactions()  # Загрузка транзакций
    history_text.delete(1.0, tk.END)  # Очистка текста
    for transaction in reversed(transactions):  # Отображаем транзакции сверху вниз
        history_text.insert(tk.END, transaction + "\n")  # Добавляем транзакцию

    # Загрузка цели и прогресса
    goal_amount, progress = load_goal()
    goal_progress_label.config(text=f"Прогресс цели: {progress:.2f}/{goal_amount:.2f}")

    # Если цель выполнена, очищаем поля
    if progress >= goal_amount:
        messagebox.showerror("Цель достигнута!", "Цель достигнута! Поздравляем😌")
        

# Функция для добавления транзакции
def add_transaction(amount, description, transaction_type):
    # Получаем текущий баланс
    balance = load_balance()

    # Проверка на расход, если расход больше баланса, то выводим ошибку
    if transaction_type == "Расход" and balance - amount < 0:
        messagebox.showerror("Ошибка", "Невозможно потратить больше, чем есть на счету!")
        return

    # Обновляем баланс
    if transaction_type == "Доход":
        balance += amount
        # Обновляем прогресс цели при добавлении дохода
        update_goal_progress(amount)
    elif transaction_type == "Расход":
        balance -= amount

    # Сохраняем обновленный баланс
    save_balance(balance)

    # Формируем строку транзакции
    transaction_str = f"{transaction_type}: {amount} ({description})"

    # Загружаем текущие транзакции
    transactions = load_transactions()

    # Добавляем новую транзакцию в список
    transactions.append(transaction_str)

    # Сохраняем обновленные транзакции
    save_transactions(transactions)

    # Обновляем UI
    update_ui()

 
# Функция для установки цели
def set_goal_amount():
    try:
        goal_amount = float(goal_amount_entry.get())  # Получаем сумму цели
        description = goal_description_entry.get()  # Получаем описание цели
        if goal_amount <= 0:
            messagebox.showwarning("Ошибка", "Цель должна быть больше нуля!")
            return
        save_goal(goal_amount, 0.0)  # Сохраняем цель с прогрессом 0
        messagebox.showinfo("Успех", "Цель установлена!")
        update_ui()
    except ValueError:
        messagebox.showerror("Ошибка", "Введите правильную сумму цели!")

# Привязка кнопок к функциям
add_transaction_button.config(command=lambda: handle_add_transaction())
set_goal_button.config(command=set_goal_amount)

# Функция для проверки и добавления транзакции
def handle_add_transaction():
    try:
        amount = float(amount_entry.get())  # Получаем сумму
        description = description_entry.get()  # Получаем описание
        if not description:
            messagebox.showwarning("Ошибка", "Описание транзакции не может быть пустым!")
            return
        add_transaction(amount, description, transaction_type.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Введите правильную сумму!")
    
# Начальная инициализация интерфейса
update_ui()

# Запуск основного цикла Tkinter
root.mainloop()
