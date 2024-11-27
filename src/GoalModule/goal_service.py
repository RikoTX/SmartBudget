# Путь к файлу цели
from tkinter import messagebox
GOAL_FILE_PATH = "C:\\Users\\User\\Desktop\\SmartBudget\\src\\DatabaseModule\\goal.txt"

# Функция для загрузки цели и прогресса
def load_goal():
    try:
        with open(GOAL_FILE_PATH, "r") as file:
            goal_data = file.read().strip().split(":")  # Разделим данные по двоеточию

            # Проверка, что goal_data[0] и goal_data[1] не пустые строки, прежде чем конвертировать в float
            goal_amount = float(goal_data[0]) if len(goal_data) > 0 and goal_data[0] else 0.0
            progress = float(goal_data[1]) if len(goal_data) > 1 and goal_data[1] else 0.0
            
            return goal_amount, progress
    except FileNotFoundError:
        return 0.0, 0.0  # Если файл не найден, возвращаем начальные значения
    except ValueError:
        # Если произошла ошибка при преобразовании строки в float, возвращаем значения по умолчанию
        return 0.0, 0.0
  # Если файл не найден, возвращаем начальные значения

# Функция для сохранения цели и прогресса
def save_goal(goal_amount, progress):
    try:
        with open(GOAL_FILE_PATH, "w") as file:
            file.write(f"{goal_amount}:{progress}")  # Сохраняем цель и прогресс через двоеточие
    except Exception as e:
        print(f"Ошибка при сохранении цели: {e}")

# Функция для обновления прогресса
def update_goal_progress(amount):
    goal_amount, progress = load_goal()  # Загрузить текущую цель и прогресс
    if goal_amount > 0:
        progress += amount  # Обновить прогресс

        # Если цель достигнута
        if progress >= goal_amount:
            progress = goal_amount  # Ограничиваем прогресс максимальной целью
            save_goal(0.0, 0.0)  # Сбросить цель (обнуляем её)

            # Показать уведомление, что цель достигнута
            messagebox.showinfo("Цель достигнута!", "Поздравляем! Вы достигли своей цели!")

        # Сохраняем обновленный прогресс
        save_goal(goal_amount, progress)
