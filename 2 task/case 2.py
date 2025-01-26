
# Есть файлы с данными f.json. Требуется написать программу на python, в которой будет производится расчет:
# - количества предметов для каждой категории
# - общая сумма продаж для каждой категории
import pandas as pd


def calculate_category_stats(file_path):
    # Читаем JSON-файл (обычный массив объектов)
    df = pd.read_json(file_path)

    # Удаляем дубликаты
    df = df.drop_duplicates(subset=['id', 'owner', 'price', 'category'])

    # Считаем количество предметов для каждой категории
    item_counts = df.groupby('category').size().to_dict()

    # Считаем общую сумму продаж для каждой категории
    total_sales = df.groupby('category')['price'].sum().to_dict()

    return item_counts, total_sales


# Пример использования
if __name__ == "__main__":
    file_path = "f.json"  # Укажи путь к своему JSON-файлу
    item_counts, total_sales = calculate_category_stats(file_path)
    print("Количество предметов для каждой категории:", item_counts)
    print("Общая сумма продаж для каждой категории:", total_sales)
