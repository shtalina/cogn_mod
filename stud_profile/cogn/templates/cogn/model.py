import matplotlib.pyplot as plt
import numpy as np

def plot_cognitive_profile(cognitive_data):
    # Получение списка категорий (названий аспектов)
    categories = list(cognitive_data.keys())

    # Получение списка значений для каждой категории
    values = list(cognitive_data.values())

    # Рассчитываем углы для каждой категории
    num_categories = len(categories)
    angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()
    angles += angles[:1]  # Добавляем первый угол в конец списка для замыкания графика

    # Создание экземпляра графика
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'polar': True})

    # Размещение категорий на окружности
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)

    # Определение максимального значения для оси
    max_value = max(values)
    ax.set_ylim(0, max_value)

    # Построение графика
    ax.plot(angles, values + values[:1], linewidth=1, linestyle='solid', marker='o')
    ax.fill(angles, values + values[:1], alpha=0.25)

    # Добавление значений на график
    for angle, value in zip(angles, values):
        ax.annotate(str(value), xy=(angle, value), ha='center', va='center')

    # Добавление заголовка
    plt.title('Когнитивная модель студента')

    # Отображение графика
    plt.show()

# Пример использования
cognitive_data = {
    "Логическое мышление": 80,
    "Математические навыки": 70,
    "Визуальное восприятие": 90,
    "Речевые способности": 75,
    "Пространственное мышление": 85,
}

# Построение графика когнитивной модели студента
plot_cognitive_profile(cognitive_data)