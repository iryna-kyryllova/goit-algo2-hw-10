# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = set()  # Предмети, які викладач буде викладати


def create_schedule(subjects, teachers):
    # Набір невикритих предметів
    remaining_subjects = set(subjects)
    schedule = []

    while remaining_subjects:
        # Вибір найкращого викладача
        best_teacher = None
        best_coverage = 0

        for teacher in teachers:
            # Підраховуємо кількість предметів, які викладач може викладати і які ще не покриті
            teachable = teacher.can_teach_subjects & remaining_subjects
            if len(teachable) > best_coverage:
                best_teacher = teacher
                best_coverage = len(teachable)
            elif len(teachable) == best_coverage and best_teacher:
                # У випадку рівної кількості предметів вибираємо молодшого викладача
                if teacher.age < best_teacher.age:
                    best_teacher = teacher

        if not best_teacher:
            # Якщо не залишилось викладачів, здатних викладати невикриті предмети
            return None

        # Призначаємо викладача на предмети
        assigned_subjects = best_teacher.can_teach_subjects & remaining_subjects
        best_teacher.assigned_subjects = assigned_subjects
        remaining_subjects -= assigned_subjects

        schedule.append(best_teacher)

    return schedule


if __name__ == "__main__":
    # Множина предметів
    subjects = {"Математика", "Фізика", "Хімія", "Інформатика", "Біологія"}
    # Створення списку викладачів
    teachers = [
        Teacher(
            "Олександр",
            "Іваненко",
            45,
            "o.ivanenko@example.com",
            {"Математика", "Фізика"},
        ),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {"Хімія"}),
        Teacher(
            "Сергій",
            "Коваленко",
            50,
            "s.kovalenko@example.com",
            {"Інформатика", "Математика"},
        ),
        Teacher(
            "Наталія", "Шевченко", 29, "n.shevchenko@example.com", {"Біологія", "Хімія"}
        ),
        Teacher(
            "Дмитро",
            "Бондаренко",
            35,
            "d.bondarenko@example.com",
            {"Фізика", "Інформатика"},
        ),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {"Біологія"}),
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(
                f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}"
            )
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
