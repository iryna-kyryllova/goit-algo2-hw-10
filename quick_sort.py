import random
import time
import numpy as np
import matplotlib.pyplot as plt


# Рандомізований QuickSort
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


# Детермінований QuickSort
def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


# Функція для вимірювання часу виконання
def measure_time(sort_function, arr):
    times = []
    for _ in range(5):
        start = time.time()
        sort_function(arr.copy())
        end = time.time()
        times.append(end - start)
    # Повертаємо середній час виконання
    return sum(times) / len(times)


# Розміри масивів для тестування
sizes = [10_000, 50_000, 100_000, 500_000]

randomized_times = []
deterministic_times = []

# Генерація та тестування масивів
for size in sizes:
    # Створюємо масив випадкових чисел
    arr = np.random.randint(0, 1_000_000, size).tolist()
    print(f"Розмір масиву: {size}")

    # Вимірюємо час для рандомізованого QuickSort
    rand_time = measure_time(randomized_quick_sort, arr)
    randomized_times.append(rand_time)
    print(f"   Рандомізований QuickSort: {rand_time:.4f} секунд")

    # Вимірюємо час для детермінованого QuickSort
    det_time = measure_time(deterministic_quick_sort, arr)
    deterministic_times.append(det_time)
    print(f"   Детермінований QuickSort: {det_time:.4f} секунд")

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(sizes, randomized_times, label="Рандомізований QuickSort")
plt.plot(sizes, deterministic_times, label="Детермінований QuickSort")

plt.title("Порівняння швидкості виконання QuickSort")
plt.xlabel("Розмір масиву")
plt.ylabel("Середній час виконання (секунди)")
plt.legend()
plt.grid(True)
plt.show()

# Висновки

# - Детермінований QuickSort показав кращу продуктивність на всіх масивах.
# - Різниця в часі між детермінованим та рандомізованим QuickSort незначна, але детермінований алгоритм стабільно працював швидше на кожному наборі даних.
# - Для великих масивів (500000 елементів) різниця в часі стає більш помітною:
#   Рандомізований: 2.4409 секунд
#   Детермінований: 2.2231 секунд.
# - Обидва алгоритми показали стабільний час виконання, що підтверджує їхню теоретичну часову складність.
# - Для вже відсортованих масивів рандомізований алгоритм може мати перевагу, оскільки він знижує ймовірність найгіршого випадку.
